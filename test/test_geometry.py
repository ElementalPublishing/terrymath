from terrymath import TerryMath, TerryVector3
from terrygeometry import (
    TerryPoint, TerryLine, TerrySegment, TerryRay, TerryPlane,
    TerrySphere, TerryBox, TerryTriangle, terry_cube, terry_quad,
    terry_distance, terry_angle
)

def test_point_addition():
    tm = TerryMath()
    p1 = TerryPoint(1, 2, 0, math_engine=tm)
    p2 = TerryPoint(3, 4, 0, math_engine=tm)
    result = p1 + p2
    assert result.x == tm.terry_add(1, 3)
    assert result.y == tm.terry_add(2, 4)
    assert result.z == tm.terry_add(0, 0)

def test_line_point_at():
    tm = TerryMath()
    p = TerryPoint(0, 0, 0, math_engine=tm)
    d = TerryVector3(1, 0, 0, tm)
    line = TerryLine(p, d, math_engine=tm)
    pt = line.point_at(2)
    assert pt.x == 2 and pt.y == 0 and pt.z == 0

def test_segment_midpoint():
    tm = TerryMath()
    s = TerrySegment(TerryVector3(0, 0, 0, tm), TerryVector3(2, 2, 2, tm), math_engine=tm)
    mid = s.midpoint()
    assert mid.x == 1 and mid.y == 1 and mid.z == 1

def test_ray_init():
    tm = TerryMath()
    origin = TerryVector3(0, 0, 0, tm)
    direction = TerryVector3(1, 0, 0, tm)
    ray = TerryRay(origin, direction, math_engine=tm)
    assert ray.origin.x == 0 and ray.direction.x == 1

def test_plane_distance_and_project():
    tm = TerryMath()
    point = TerryVector3(0, 0, 0, tm)
    normal = TerryVector3(0, 1, 0, tm)
    plane = TerryPlane(point, normal, math_engine=tm)
    pt = TerryVector3(0, 2, 0, tm)
    dist = plane.distance_to_point(pt)
    proj = plane.project_point(pt)
    assert dist == 2
    assert proj.y == 0

def test_plane_intersect_ray():
    tm = TerryMath()
    plane = TerryPlane(TerryVector3(0, 0, 0, tm), TerryVector3(0, 1, 0, tm), math_engine=tm)
    ray = TerryRay(TerryVector3(0, -1, 0, tm), TerryVector3(0, 1, 0, tm), math_engine=tm)
    t = plane.intersect_ray(ray)
    assert t == 1

def test_sphere_contains_and_intersect():
    tm = TerryMath()
    center = TerryVector3(0, 0, 0, tm)
    sphere = TerrySphere(center, 1, math_engine=tm)
    pt_inside = TerryVector3(0, 0, 0, tm)
    pt_outside = TerryVector3(2, 0, 0, tm)
    assert sphere.contains_point(pt_inside)
    assert not sphere.contains_point(pt_outside)
    ray = TerryRay(TerryVector3(-2, 0, 0, tm), TerryVector3(1, 0, 0, tm), math_engine=tm)
    result = sphere.intersect_ray(ray)
    assert result is not None

def test_box_contains_and_intersect():
    tm = TerryMath()
    min_corner = TerryVector3(0, 0, 0, tm)
    max_corner = TerryVector3(1, 1, 1, tm)
    box = TerryBox(min_corner, max_corner, math_engine=tm)
    pt_inside = TerryVector3(0.5, 0.5, 0.5, tm)
    pt_outside = TerryVector3(2, 2, 2, tm)
    assert box.contains_point(pt_inside)
    assert not box.contains_point(pt_outside)
    ray = TerryRay(TerryVector3(-1, 0.5, 0.5, tm), TerryVector3(1, 0, 0, tm), math_engine=tm)
    result = box.intersect_ray(ray)
    assert result is not None

def test_triangle_area_and_contains():
    tm = TerryMath()
    v0 = TerryVector3(0, 0, 0, tm)
    v1 = TerryVector3(1, 0, 0, tm)
    v2 = TerryVector3(0, 1, 0, tm)
    tri = TerryTriangle(v0, v1, v2, math_engine=tm)
    area = tri.area()
    assert area > 0
    pt_inside = TerryVector3(0.2, 0.2, 0, tm)
    pt_outside = TerryVector3(2, 2, 0, tm)
    assert tri.contains_point(pt_inside)
    assert not tri.contains_point(pt_outside)

def test_triangle_intersect_ray():
    tm = TerryMath()
    v0 = TerryVector3(0, 0, 0, tm)
    v1 = TerryVector3(1, 0, 0, tm)
    v2 = TerryVector3(0, 1, 0, tm)
    tri = TerryTriangle(v0, v1, v2, math_engine=tm)
    ray = TerryRay(TerryVector3(0.1, 0.1, -1, tm), TerryVector3(0, 0, 1, tm), math_engine=tm)
    t = tri.intersect_ray(ray)
    assert t is not None

def test_terry_cube_and_quad():
    tm = TerryMath()
    center = TerryVector3(0, 0, 0, tm)
    corners = terry_cube(center, 2, math_engine=tm)
    assert len(corners) == 8
    quad = terry_quad(center, 2, TerryVector3(0, 0, 1, tm), math_engine=tm)
    assert len(quad) == 4

def test_terry_distance_and_angle():
    tm = TerryMath()
    a = TerryVector3(0, 0, 0, tm)
    b = TerryVector3(1, 0, 0, tm)
    dist = terry_distance(a, b, math_engine=tm)
    angle = terry_angle(a, b, math_engine=tm)
    assert dist == 1
    import math
    assert angle == 0.0
    print("a:", a)
    print("b:", b)
    print("b - a:", b - a)
    print("dot:", (b - a).dot(b - a))
    print("dist:", dist)
    expected = (b - a).dot(b - a) ** 0.5
    assert math.isclose(dist, expected)