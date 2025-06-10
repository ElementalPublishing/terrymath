import math
from terrymath import TerryMath, TerryVector3

class TerryMatrix4x4:
    def __init__(self, rows, math_engine=None):
        assert len(rows) == 4 and all(len(row) == 4 for row in rows)
        self.data = [list(row) for row in rows]
        self.math = math_engine or TerryMath()

    def __add__(self, other):
        return TerryMatrix4x4(
            [
                [self.math.terry_add(self.data[i][j], other.data[i][j]) for j in range(4)]
                for i in range(4)
            ],
            self.math
        )

    def __mul__(self, other):
        tm = self.math
        if isinstance(other, TerryMatrix4x4):
            result = [[0]*4 for _ in range(4)]
            for i in range(4):
                for j in range(4):
                    result[i][j] = tm.terry_add(
                        tm.terry_add(
                            tm.terry_add(
                                tm.terry_multiply(self.data[i][0], other.data[0][j]),
                                tm.terry_multiply(self.data[i][1], other.data[1][j])
                            ),
                            tm.terry_multiply(self.data[i][2], other.data[2][j])
                        ),
                        tm.terry_multiply(self.data[i][3], other.data[3][j])
                    )
            return TerryMatrix4x4(result, tm)
        elif isinstance(other, TerryVector3):
            # Matrix-vector multiplication (assume w=1)
            x = tm.terry_add(
                tm.terry_add(
                    tm.terry_add(
                        tm.terry_multiply(self.data[0][0], other.x),
                        tm.terry_multiply(self.data[0][1], other.y)
                    ),
                    tm.terry_multiply(self.data[0][2], other.z)
                ),
                self.data[0][3]
            )
            y = tm.terry_add(
                tm.terry_add(
                    tm.terry_add(
                        tm.terry_multiply(self.data[1][0], other.x),
                        tm.terry_multiply(self.data[1][1], other.y)
                    ),
                    tm.terry_multiply(self.data[1][2], other.z)
                ),
                self.data[1][3]
            )
            z = tm.terry_add(
                tm.terry_add(
                    tm.terry_add(
                        tm.terry_multiply(self.data[2][0], other.x),
                        tm.terry_multiply(self.data[2][1], other.y)
                    ),
                    tm.terry_multiply(self.data[2][2], other.z)
                ),
                self.data[2][3]
            )
            return TerryVector3(x, y, z, tm)
        else:
            raise TypeError("Unsupported multiplication")

    def transpose(self):
        tm = self.math
        return TerryMatrix4x4(
            [[self.data[j][i] for j in range(4)] for i in range(4)],
            tm
        )

    def determinant(self):
        # Laplace expansion (not optimized, but Terry-correct)
        m = self.data
        tm = self.math

        def det3x3(sub):
            return (
                tm.terry_add(
                    tm.terry_add(
                        tm.terry_multiply(sub[0][0], tm.terry_subtract(
                            tm.terry_multiply(sub[1][1], sub[2][2]),
                            tm.terry_multiply(sub[1][2], sub[2][1])
                        )),
                        -tm.terry_multiply(sub[0][1], tm.terry_subtract(
                            tm.terry_multiply(sub[1][0], sub[2][2]),
                            tm.terry_multiply(sub[1][2], sub[2][0])
                        ))
                    ),
                    tm.terry_multiply(sub[0][2], tm.terry_subtract(
                        tm.terry_multiply(sub[1][0], sub[2][1]),
                        tm.terry_multiply(sub[1][1], sub[2][0])
                    ))
                )
            )

        det = 0
        for col in range(4):
            # Build 3x3 minor
            minor = [
                [m[row][c] for c in range(4) if c != col]
                for row in range(1, 4)
            ]
            sign = (-1) ** col
            det = tm.terry_add(
                det,
                tm.terry_multiply(sign * m[0][col], det3x3(minor))
            )
        return det

    def identity(math_engine=None):
        tm = math_engine or TerryMath()
        return TerryMatrix4x4([
            [1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [0,0,0,1]
        ], tm)

    def zero(math_engine=None):
        tm = math_engine or TerryMath()
        return TerryMatrix4x4([
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
        ], tm)

    def to_flat_list(self):
        return [self.data[i][j] for i in range(4) for j in range(4)]

    def copy(self):
        return TerryMatrix4x4([row[:] for row in self.data], self.math)

    def __repr__(self):
        return f"TerryMatrix4x4({self.data[0]}, {self.data[1]}, {self.data[2]}, {self.data[3]})"


class TerryQuaternion:
    def __init__(self, w, x, y, z, math_engine=None):
        self.w = w
        self.x = x
        self.y = y
        self.z = z
        self.math = math_engine or TerryMath()

    def __mul__(self, other):
        tm = self.math
        w = tm.terry_subtract(
                tm.terry_subtract(
                    tm.terry_subtract(
                        tm.terry_multiply(self.w, other.w),
                        tm.terry_multiply(self.x, other.x)
                    ),
                    tm.terry_multiply(self.y, other.y)
                ),
                tm.terry_multiply(self.z, other.z)
            )
        x = tm.terry_add(
                tm.terry_add(
                    tm.terry_add(
                        tm.terry_multiply(self.w, other.x),
                        tm.terry_multiply(self.x, other.w)
                    ),
                    tm.terry_multiply(self.y, other.z)
                ),
                -tm.terry_multiply(self.z, other.y)
            )
        y = tm.terry_add(
                tm.terry_add(
                    tm.terry_add(
                        tm.terry_multiply(self.w, other.y),
                        -tm.terry_multiply(self.x, other.z)
                    ),
                    tm.terry_multiply(self.y, other.w)
                ),
                tm.terry_multiply(self.z, other.x)
            )
        z = tm.terry_add(
                tm.terry_add(
                    tm.terry_add(
                        tm.terry_multiply(self.w, other.z),
                        tm.terry_multiply(self.x, other.y)
                    ),
                    -tm.terry_multiply(self.y, other.x)
                ),
                tm.terry_multiply(self.z, other.w)
            )
        return TerryQuaternion(w, x, y, z, tm)

    def conjugate(self):
        tm = self.math
        return TerryQuaternion(self.w, -self.x, -self.y, -self.z, tm)

    def norm(self):
        tm = self.math
        return (tm.terry_add(
            tm.terry_add(
                tm.terry_multiply(self.w, self.w),
                tm.terry_multiply(self.x, self.x)
            ),
            tm.terry_add(
                tm.terry_multiply(self.y, self.y),
                tm.terry_multiply(self.z, self.z)
            )
        )) ** 0.5

    def normalize(self):
        n = self.norm()
        if n == 0:
            return TerryQuaternion(1, 0, 0, 0, self.math)
        return TerryQuaternion(self.w / n, self.x / n, self.y / n, self.z / n, self.math)

    def __repr__(self):
        return f"TerryQuaternion({self.w}, {self.x}, {self.y}, {self.z})"

def terry_lerp_vec3(a, b, t):
    """Linear interpolation between two TerryVector3s."""
    return a + (b - a) * t

def terry_slerp_quat(q1, q2, t):
    """Spherical linear interpolation between two TerryQuaternions."""
    tm = q1.math
    dot = tm.terry_add(
        tm.terry_add(
            tm.terry_multiply(q1.w, q2.w),
            tm.terry_multiply(q1.x, q2.x)
        ),
        tm.terry_add(
            tm.terry_multiply(q1.y, q2.y),
            tm.terry_multiply(q1.z, q2.z)
        )
    )
    if dot < 0.0:
        q2 = TerryQuaternion(-q2.w, -q2.x, -q2.y, -q2.z, tm)
        dot = -dot
    if dot > 0.9995:
        # Linear interpolation for very close quaternions
        result = TerryQuaternion(
            q1.w + t*(q2.w - q1.w),
            q1.x + t*(q2.x - q1.x),
            q1.y + t*(q2.y - q1.y),
            q1.z + t*(q2.z - q1.z),
            tm
        ).normalize()
        return result
    theta_0 = math.acos(dot)
    theta = theta_0 * t
    sin_theta = math.sin(theta)
    sin_theta_0 = math.sin(theta_0)
    s0 = math.cos(theta) - dot * sin_theta / sin_theta_0
    s1 = sin_theta / sin_theta_0
    return TerryQuaternion(
        (q1.w * s0) + (q2.w * s1),
        (q1.x * s0) + (q2.x * s1),
        (q1.y * s0) + (q2.y * s1),
        (q1.z * s0) + (q2.z * s1),
        tm
    ).normalize()

def terry_rotation_matrix(axis, angle, math_engine=None):
    """Terry-based 3D rotation matrix from axis and angle (Rodrigues' formula)."""
    tm = math_engine or TerryMath()
    x, y, z = axis.normalize().x, axis.normalize().y, axis.normalize().z
    c = math.cos(angle)
    s = math.sin(angle)
    t = 1 - c
    return TerryMatrix4x4([
        [t*x*x + c,   t*x*y - s*z, t*x*z + s*y, 0],
        [t*x*y + s*z, t*y*y + c,   t*y*z - s*x, 0],
        [t*x*z - s*y, t*y_z + s*x, t*z*z + c,   0],
        [0,           0,           0,           1]
    ], tm)
