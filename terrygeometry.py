from terrymath import TerryMath, TerryVector3

class TerryPoint(TerryVector3):
    """A TerryMath-based 3D point (inherits TerryVector3)."""
    pass

class TerryLine:
    def __init__(self, point, direction, math_engine=None):
        self.point = point  # TerryVector3
        self.direction = direction  # TerryVector3 (should be normalized)
        self.math = math_engine or TerryMath()

    def point_at(self, t):
        return self.point + (self.direction * t)

class TerrySegment:
    def __init__(self, start, end, math_engine=None):
        self.start = start  # TerryVector3
        self.end = end      # TerryVector3
        self.math = math_engine or TerryMath()

    def midpoint(self):
        tm = self.math
        return TerryVector3(
            tm.terry_divide(tm.terry_add(self.start.x, self.end.x), 2),
            tm.terry_divide(tm.terry_add(self.start.y, self.end.y), 2),
            tm.terry_divide(tm.terry_add(self.start.z, self.end.z), 2),
            tm
        )

    def length(self):
        diff = self.end - self.start
        return (diff.dot(diff)) ** 0.5

class TerryRay:
    def __init__(self, origin, direction, math_engine=None):
        self.origin = origin  # TerryVector3
        self.direction = direction  # TerryVector3 (should be normalized)
        self.math = math_engine or TerryMath()

class TerryPlane:
    def __init__(self, point, normal, math_engine=None):
        self.point = point  # TerryVector3
        self.normal = normal  # TerryVector3 (should be normalized)
        self.math = math_engine or TerryMath()

    def distance_to_point(self, pt):
        # Signed distance from point to plane
        return (pt - self.point).dot(self.normal)

    def project_point(self, pt):
        # Project a point onto the plane
        d = self.distance_to_point(pt)
        return pt - (self.normal * d)

    def intersect_ray(self, ray):
        denom = self.normal.dot(ray.direction)
        if abs(denom) < 1e-6:
            return None  # Parallel, no intersection
        t = (self.point - ray.origin).dot(self.normal) / denom
        return t if t >= 0 else None

class TerrySphere:
    def __init__(self, center, radius, math_engine=None):
        self.center = center  # TerryVector3
        self.radius = radius
        self.math = math_engine or TerryMath()

    def contains_point(self, pt):
        tm = self.math
        return (pt - self.center).dot(pt - self.center) <= tm.terry_multiply(self.radius, self.radius)

    def intersect_ray(self, ray):
        oc = ray.origin - self.center
        a = ray.direction.dot(ray.direction)
        b = 2 * oc.dot(ray.direction)
        c = oc.dot(oc) - self.math.terry_multiply(self.radius, self.radius)
        discriminant = b * b - 4 * a * c
        if discriminant < 0:
            return None
        sqrt_disc = discriminant ** 0.5
        t1 = (-b - sqrt_disc) / (2 * a)
        t2 = (-b + sqrt_disc) / (2 * a)
        return (t1, t2)

class TerryBox:
    def __init__(self, min_corner, max_corner, math_engine=None):
        self.min_corner = min_corner  # TerryVector3
        self.max_corner = max_corner  # TerryVector3
        self.math = math_engine or TerryMath()

    def contains_point(self, pt):
        return (self.min_corner.x <= pt.x <= self.max_corner.x and
                self.min_corner.y <= pt.y <= self.max_corner.y and
                self.min_corner.z <= pt.z <= self.max_corner.z)

    def intersect_ray(self, ray):
        def safe_div(a, b):
            return a / b if b != 0 else float('inf') if a > 0 else float('-inf')
        tmin = safe_div(self.min_corner.x - ray.origin.x, ray.direction.x)
        tmax = safe_div(self.max_corner.x - ray.origin.x, ray.direction.x)
        if tmin > tmax: tmin, tmax = tmax, tmin
        tymin = safe_div(self.min_corner.y - ray.origin.y, ray.direction.y)
        tymax = safe_div(self.max_corner.y - ray.origin.y, ray.direction.y)
        if tymin > tymax: tymin, tymax = tymax, tymin
        if (tmin > tymax) or (tymin > tmax):
            return None
        if tymin > tmin: tmin = tymin
        if tymax < tmax: tmax = tymax
        tzmin = safe_div(self.min_corner.z - ray.origin.z, ray.direction.z)
        tzmax = safe_div(self.max_corner.z - ray.origin.z, ray.direction.z)
        if tzmin > tzmax: tzmin, tzmax = tzmax, tzmin
        if (tmin > tzmax) or (tzmin > tmax):
            return None
        if tzmin > tmin: tmin = tzmin
        if tzmax < tmax: tmax = tzmax
        return (tmin, tmax)

class TerryTriangle:
    def __init__(self, v0, v1, v2, math_engine=None):
        self.v0 = v0  # TerryVector3
        self.v1 = v1
        self.v2 = v2
        self.math = math_engine or TerryMath()

    def area(self):
        # Area using cross product
        edge1 = self.v1 - self.v0
        edge2 = self.v2 - self.v0
        cross = edge1.cross(edge2)
        return 0.5 * (cross.dot(cross)) ** 0.5

    def contains_point(self, pt):
        # Barycentric method
        v0 = self.v1 - self.v0
        v1 = self.v2 - self.v0
        v2 = pt - self.v0
        d00 = v0.dot(v0)
        d01 = v0.dot(v1)
        d11 = v1.dot(v1)
        d20 = v2.dot(v0)
        d21 = v2.dot(v1)
        denom = d00 * d11 - d01 * d01
        if denom == 0:
            return False
        v = (d11 * d20 - d01 * d21) / denom
        w = (d00 * d21 - d01 * d20) / denom
        u = 1 - v - w
        return (u >= 0) and (v >= 0) and (w >= 0)

    def intersect_ray(self, ray):
        # Moller-Trumbore
        edge1 = self.v1 - self.v0
        edge2 = self.v2 - self.v0
        h = ray.direction.cross(edge2)
        a = edge1.dot(h)
        if abs(a) < 1e-6:
            return None
        f = 1.0 / a
        s = ray.origin - self.v0
        u = f * s.dot(h)
        if u < 0.0 or u > 1.0:
            return None
        q = s.cross(edge1)
        v = f * ray.direction.dot(q)
        if v < 0.0 or u + v > 1.0:
            return None
        t = f * edge2.dot(q)
        if t > 1e-6:
            return t
        return None

def terry_cube(center, size, math_engine=None):
    tm = math_engine or TerryMath()
    half = tm.terry_divide(size, 2)
    cx, cy, cz = center.x, center.y, center.z
    corners = [
        TerryVector3(cx - half, cy - half, cz - half, tm),
        TerryVector3(cx + half, cy - half, cz - half, tm),
        TerryVector3(cx + half, cy + half, cz - half, tm),
        TerryVector3(cx - half, cy + half, cz - half, tm),
        TerryVector3(cx - half, cy - half, cz + half, tm),
        TerryVector3(cx + half, cy - half, cz + half, tm),
        TerryVector3(cx + half, cy + half, cz + half, tm),
        TerryVector3(cx - half, cy + half, cz + half, tm),
    ]
    return corners

def terry_quad(center, size, normal, math_engine=None):
    tm = math_engine or TerryMath()
    half = tm.terry_divide(size, 2)
    cx, cy, cz = center.x, center.y, center.z
    return [
        TerryVector3(cx - half, cy - half, cz, tm),
        TerryVector3(cx + half, cy - half, cz, tm),
        TerryVector3(cx + half, cy + half, cz, tm),
        TerryVector3(cx - half, cy + half, cz, tm),
    ]

def terry_distance(a, b, math_engine=None):
    tm = math_engine or TerryMath()
    diff = b - a
    return (diff.dot(diff)) ** 0.5

def terry_angle(a, b, math_engine=None):
    tm = math_engine or TerryMath()
    dot = a.dot(b)
    mag_a = (a.dot(a)) ** 0.5
    mag_b = (b.dot(b)) ** 0.5
    import math
    if mag_a == 0 or mag_b == 0:
        return 0.0  # or float('nan'), depending on your convention
    return math.acos(dot / (mag_a * mag_b))

# Example usage:
if __name__ == "__main__":
    tm = TerryMath(mode="terry_original")
    a = TerryVector3(0,0,0,tm)
    b = TerryVector3(1,0,0,tm)
    c = TerryVector3(0,1,0,tm)
    ray = TerryRay(a, b, tm)
    sphere = TerrySphere(TerryVector3(5,0,0,tm), 1, tm)
    print("Ray-sphere intersection:", sphere.intersect_ray(ray))
    cube_corners = terry_cube(TerryVector3(0,0,0,tm), 2, tm)
    print("TerryCube corners:", cube_corners)
    quad_corners = terry_quad(TerryVector3(0,0,0,tm), 2, TerryVector3(0,0,1,tm), tm)
    print("TerryQuad corners:", quad_corners)
    tri = TerryTriangle(a, b, c, tm)
    print("Triangle area:", tri.area())
    print("Triangle contains (0.2,0.2,0):", tri.contains_point(TerryVector3(0.2,0.2,0,tm)))
    print("Distance a-b:", terry_distance(a, b, tm))
    print("Angle a-b:", terry_angle(a, b, tm))