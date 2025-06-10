class TerryMath:
    """
    TerryMath Engine: Foundation for all arithmetic and algebraic operations.
    Supports custom multiplication/addition rules (modes).
    """

    MODES = {
        "a_plus_b_minus_1": lambda a, b: a + b - 1,
        "a_plus_b": lambda a, b: a + b,
        "a_times_b": lambda a, b: a * b,
        "terry_original": lambda a, b: 2 if a == 1 and b == 1 else a * b,
    }

    def __init__(self, mode="terry_original"):
        self.set_mode(mode)

    def set_mode(self, mode):
        if mode not in self.MODES:
            raise ValueError(f"Unknown Terry Table mode: {mode}")
        self.mode = mode
        self.multiply_rule = self.MODES[mode]

    def terry_multiply(self, a, b):
        return self.multiply_rule(a, b)

    def terry_add(self, a, b):
        return a + b

    def terry_subtract(self, a, b):
        return a - b

    def terry_divide(self, a, b):
        return a / b

    def terry_power(self, a, b):
        if b == 0:
            return 1
        result = a
        for _ in range(1, b):
            result = self.terry_multiply(result, a)
        return result

    @staticmethod
    def list_modes():
        return list(TerryMath.MODES.keys())

class TerryVector2:
    def __init__(self, x, y, math_engine=None):
        self.x = x
        self.y = y
        self.math = math_engine or TerryMath()

    def __add__(self, other):
        if not isinstance(other, TerryVector2):
            raise TypeError("Can only add TerryVector2 to TerryVector2")
        return TerryVector2(
            self.math.terry_add(self.x, other.x),
            self.math.terry_add(self.y, other.y),
            self.math
        )

    def __sub__(self, other):
        if not isinstance(other, TerryVector2):
            raise TypeError("Can only subtract TerryVector2 from TerryVector2")
        return TerryVector2(
            self.math.terry_subtract(self.x, other.x),
            self.math.terry_subtract(self.y, other.y),
            self.math
        )

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Can only multiply TerryVector2 by a scalar")
        return TerryVector2(
            self.math.terry_multiply(self.x, scalar),
            self.math.terry_multiply(self.y, scalar),
            self.math
        )

    def __neg__(self):
        return TerryVector2(
            self.math.terry_multiply(-1, self.x),
            self.math.terry_multiply(-1, self.y),
            self.math
        )

    def dot(self, other):
        if not isinstance(other, TerryVector2):
            raise TypeError("Can only take dot product with another TerryVector2")
        return self.math.terry_add(
            self.math.terry_multiply(self.x, other.x),
            self.math.terry_multiply(self.y, other.y)
        )

    def __repr__(self):
        return f"TerryVector2({self.x}, {self.y})"

class TerryVector3:
    def __init__(self, x, y, z, math_engine=None):
        self.x = x
        self.y = y
        self.z = z
        self.math = math_engine or TerryMath()

    def __add__(self, other):
        if not isinstance(other, TerryVector3):
            raise TypeError("Can only add TerryVector3 to TerryVector3")
        return TerryVector3(
            self.math.terry_add(self.x, other.x),
            self.math.terry_add(self.y, other.y),
            self.math.terry_add(self.z, other.z),
            self.math
        )

    def __sub__(self, other):
        if not isinstance(other, TerryVector3):
            raise TypeError("Can only subtract TerryVector3 from TerryVector3")
        return TerryVector3(
            self.math.terry_subtract(self.x, other.x),
            self.math.terry_subtract(self.y, other.y),
            self.math.terry_subtract(self.z, other.z),
            self.math
        )

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Can only multiply TerryVector3 by a scalar")
        return TerryVector3(
            self.math.terry_multiply(self.x, scalar),
            self.math.terry_multiply(self.y, scalar),
            self.math.terry_multiply(self.z, scalar),
            self.math
        )

    def dot(self, other):
        if not isinstance(other, TerryVector3):
            raise TypeError("Can only take dot product with another TerryVector3")
        return self.math.terry_add(
            self.math.terry_add(
                self.math.terry_multiply(self.x, other.x),
                self.math.terry_multiply(self.y, other.y)
            ),
            self.math.terry_multiply(self.z, other.z)
        )

    def cross(self, other):
        if not isinstance(other, TerryVector3):
            raise TypeError("Can only take cross product with another TerryVector3")
        x = self.math.terry_subtract(
            self.math.terry_multiply(self.y, other.z),
            self.math.terry_multiply(self.z, other.y)
        )
        y = self.math.terry_subtract(
            self.math.terry_multiply(self.z, other.x),
            self.math.terry_multiply(self.x, other.z)
        )
        z = self.math.terry_subtract(
            self.math.terry_multiply(self.x, other.y),
            self.math.terry_multiply(self.y, other.x)
        )
        return TerryVector3(x, y, z, self.math)

    def __repr__(self):
        return f"TerryVector3({self.x}, {self.y}, {self.z})"

class TerryMatrix2x2:
    def __init__(self, a11, a12, a21, a22, math_engine=None):
        self.data = [
            [a11, a12],
            [a21, a22]
        ]
        self.math = math_engine or TerryMath()

    def __add__(self, other):
        if not isinstance(other, TerryMatrix2x2):
            raise TypeError("Can only add TerryMatrix2x2 to TerryMatrix2x2")
        return TerryMatrix2x2(
            self.math.terry_add(self.data[0][0], other.data[0][0]),
            self.math.terry_add(self.data[0][1], other.data[0][1]),
            self.math.terry_add(self.data[1][0], other.data[1][0]),
            self.math.terry_add(self.data[1][1], other.data[1][1]),
            self.math
        )

    def __mul__(self, other):
        if isinstance(other, TerryMatrix2x2):
            m = self
            n = other
            return TerryMatrix2x2(
                self.math.terry_add(
                    self.math.terry_multiply(m.data[0][0], n.data[0][0]),
                    self.math.terry_multiply(m.data[0][1], n.data[1][0])
                ),
                self.math.terry_add(
                    self.math.terry_multiply(m.data[0][0], n.data[0][1]),
                    self.math.terry_multiply(m.data[0][1], n.data[1][1])
                ),
                self.math.terry_add(
                    self.math.terry_multiply(m.data[1][0], n.data[0][0]),
                    self.math.terry_multiply(m.data[1][1], n.data[1][0])
                ),
                self.math.terry_add(
                    self.math.terry_multiply(m.data[1][0], n.data[0][1]),
                    self.math.terry_multiply(m.data[1][1], n.data[1][1])
                ),
                self.math
            )
        elif isinstance(other, TerryVector2):
            x = self.math.terry_add(
                self.math.terry_multiply(self.data[0][0], other.x),
                self.math.terry_multiply(self.data[0][1], other.y)
            )
            y = self.math.terry_add(
                self.math.terry_multiply(self.data[1][0], other.x),
                self.math.terry_multiply(self.data[1][1], other.y)
            )
            return TerryVector2(x, y, self.math)
        else:
            raise TypeError("Unsupported multiplication for TerryMatrix2x2")

    def determinant(self):
        a = self.math.terry_multiply(self.data[0][0], self.data[1][1])
        b = self.math.terry_multiply(self.data[0][1], self.data[1][0])
        return self.math.terry_subtract(a, b)

    def inverse(self):
        det = self.determinant()
        if det == 0:
            raise ValueError("Matrix is singular and cannot be inverted (det=0).")
        tm = self.math
        inv_det = tm.terry_divide(1, det)
        a, b = self.data[0]
        c, d = self.data[1]
        return TerryMatrix2x2(
            tm.terry_multiply(d, inv_det),
            tm.terry_multiply(-b, inv_det),
            tm.terry_multiply(-c, inv_det),
            tm.terry_multiply(a, inv_det),
            tm
        )

    def __repr__(self):
        return f"TerryMatrix2x2({self.data[0][0]}, {self.data[0][1]}, {self.data[1][0]}, {self.data[1][1]})"

class TerryMatrix3x3:
    def __init__(self, rows, math_engine=None):
        assert len(rows) == 3 and all(len(row) == 3 for row in rows)
        self.data = [list(row) for row in rows]
        self.math = math_engine or TerryMath()

    def __add__(self, other):
        if not isinstance(other, TerryMatrix3x3):
            raise TypeError("Can only add TerryMatrix3x3 to TerryMatrix3x3")
        return TerryMatrix3x3(
            [
                [self.math.terry_add(self.data[i][j], other.data[i][j]) for j in range(3)]
                for i in range(3)
            ],
            self.math
        )

    def __mul__(self, other):
        if isinstance(other, TerryMatrix3x3):
            result = [[0]*3 for _ in range(3)]
            for i in range(3):
                for j in range(3):
                    result[i][j] = self.math.terry_add(
                        self.math.terry_add(
                            self.math.terry_multiply(self.data[i][0], other.data[0][j]),
                            self.math.terry_multiply(self.data[i][1], other.data[1][j])
                        ),
                        self.math.terry_multiply(self.data[i][2], other.data[2][j])
                    )
            return TerryMatrix3x3(result, self.math)
        else:
            raise TypeError("Unsupported multiplication for TerryMatrix3x3")

    def determinant(self):
        m = self.data
        tm = self.math
        term1 = tm.terry_multiply(m[0][0], tm.terry_subtract(
            tm.terry_multiply(m[1][1], m[2][2]),
            tm.terry_multiply(m[1][2], m[2][1])
        ))
        term2 = tm.terry_multiply(m[0][1], tm.terry_subtract(
            tm.terry_multiply(m[1][0], m[2][2]),
            tm.terry_multiply(m[1][2], m[2][0])
        ))
        term3 = tm.terry_multiply(m[0][2], tm.terry_subtract(
            tm.terry_multiply(m[1][0], m[2][1]),
            tm.terry_multiply(m[1][1], m[2][0])
        ))
        return tm.terry_add(
            tm.terry_subtract(term1, term2),
            term3
        )

    def inverse(self):
        det = self.determinant()
        if det == 0:
            raise ValueError("Matrix is singular and cannot be inverted (det=0).")
        tm = self.math
        m = self.data

        def minor(i, j):
            return [
                [m[x][y] for y in range(3) if y != j]
                for x in range(3) if x != i
            ]
        def det2x2(sub):
            return tm.terry_subtract(
                tm.terry_multiply(sub[0][0], sub[1][1]),
                tm.terry_multiply(sub[0][1], sub[1][0])
            )

        cofactors = []
        for i in range(3):
            row = []
            for j in range(3):
                sign = (-1) ** (i + j)
                minor_det = det2x2(minor(i, j))
                row.append(tm.terry_multiply(sign, minor_det))
            cofactors.append(row)

        adjugate = [[cofactors[j][i] for j in range(3)] for i in range(3)]

        inv_det = tm.terry_divide(1, det)
        inverse = [
            [tm.terry_multiply(adjugate[i][j], inv_det) for j in range(3)]
            for i in range(3)
        ]
        return TerryMatrix3x3(inverse, tm)

    def __repr__(self):
        return f"TerryMatrix3x3({self.data[0]}, {self.data[1]}, {self.data[2]})"

# Usage in your engine:
# terry_math = TerryMath(mode="terry_original")
# v1 = TerryVector2(1, 2, terry_math)
# v2 = TerryVector2(3, 4, terry_math)
# print(v1 + v2)
# print(v1 * 2)
# print(v1.dot(v2))
# m1 = TerryMatrix2x2(1, 2, 3, 4, terry_math)
# m2 = TerryMatrix2x2(5, 6, 7, 8, terry_math)
# print(m1 + m2)
# print(m1 * m2)
# v = TerryVector2(1, 2, terry_math)
# print(m1 * v)
# m3 = TerryMatrix3x3([[1,2,3],[4,5,6],[7,8,9]], terry_math)
# print(m3 * m3)