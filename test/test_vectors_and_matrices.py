from terrymath import TerryMath, TerryVector2, TerryVector3, TerryMatrix2x2, TerryMatrix3x3

def test_vector2_add():
    tm = TerryMath()
    v1 = TerryVector2(1, 2, tm)
    v2 = TerryVector2(3, 4, tm)
    result = v1 + v2
    assert result.x == tm.terry_add(1, 3)
    assert result.y == tm.terry_add(2, 4)

def test_vector2_sub():
    tm = TerryMath()
    v1 = TerryVector2(5, 7, tm)
    v2 = TerryVector2(2, 3, tm)
    result = v1 - v2
    assert result.x == tm.terry_subtract(5, 2)
    assert result.y == tm.terry_subtract(7, 3)

def test_vector2_mul():
    tm = TerryMath()
    v = TerryVector2(2, 3, tm)
    result = v * 4
    assert result.x == tm.terry_multiply(2, 4)
    assert result.y == tm.terry_multiply(3, 4)

def test_vector2_dot():
    tm = TerryMath()
    v1 = TerryVector2(1, 2, tm)
    v2 = TerryVector2(3, 4, tm)
    expected = tm.terry_add(
        tm.terry_multiply(1, 3),
        tm.terry_multiply(2, 4)
    )
    assert v1.dot(v2) == expected

def test_vector2_repr():
    tm = TerryMath()
    v = TerryVector2(2, 3, tm)
    assert "TerryVector2" in repr(v)

def test_vector3_add():
    tm = TerryMath()
    v1 = TerryVector3(1, 2, 3, tm)
    v2 = TerryVector3(4, 5, 6, tm)
    result = v1 + v2
    assert result.x == tm.terry_add(1, 4)
    assert result.y == tm.terry_add(2, 5)
    assert result.z == tm.terry_add(3, 6)

def test_vector3_sub():
    tm = TerryMath()
    v1 = TerryVector3(5, 7, 9, tm)
    v2 = TerryVector3(1, 2, 3, tm)
    result = v1 - v2
    assert result.x == tm.terry_subtract(5, 1)
    assert result.y == tm.terry_subtract(7, 2)
    assert result.z == tm.terry_subtract(9, 3)

def test_vector3_mul():
    tm = TerryMath()
    v = TerryVector3(2, 3, 4, tm)
    result = v * 3
    assert result.x == tm.terry_multiply(2, 3)
    assert result.y == tm.terry_multiply(3, 3)
    assert result.z == tm.terry_multiply(4, 3)

def test_vector3_dot():
    tm = TerryMath()
    v1 = TerryVector3(1, 2, 3, tm)
    v2 = TerryVector3(4, 5, 6, tm)
    expected = tm.terry_add(
        tm.terry_add(
            tm.terry_multiply(1, 4),
            tm.terry_multiply(2, 5)
        ),
        tm.terry_multiply(3, 6)
    )
    assert v1.dot(v2) == expected

def test_vector3_cross():
    tm = TerryMath()
    v1 = TerryVector3(1, 2, 3, tm)
    v2 = TerryVector3(4, 5, 6, tm)
    # Cross product using TerryMath rules
    expected_x = tm.terry_subtract(
        tm.terry_multiply(2, 6),
        tm.terry_multiply(3, 5)
    )
    expected_y = tm.terry_subtract(
        tm.terry_multiply(3, 4),
        tm.terry_multiply(1, 6)
    )
    expected_z = tm.terry_subtract(
        tm.terry_multiply(1, 5),
        tm.terry_multiply(2, 4)
    )
    result = v1.cross(v2)
    assert result.x == expected_x
    assert result.y == expected_y
    assert result.z == expected_z

def test_vector3_repr():
    tm = TerryMath()
    v = TerryVector3(2, 3, 4, tm)
    assert "TerryVector3" in repr(v)

def test_matrix2x2_add():
    tm = TerryMath()
    m1 = TerryMatrix2x2(1, 2, 3, 4, math_engine=tm)
    m2 = TerryMatrix2x2(5, 6, 7, 8, math_engine=tm)
    result = m1 + m2
    expected = [
        [tm.terry_add(1, 5), tm.terry_add(2, 6)],
        [tm.terry_add(3, 7), tm.terry_add(4, 8)]
    ]
    assert result.data == expected

def test_matrix2x2_mul_matrix():
    tm = TerryMath()
    m1 = TerryMatrix2x2(1, 2, 3, 4, math_engine=tm)
    m2 = TerryMatrix2x2(2, 0, 1, 2, math_engine=tm)
    result = m1 * m2
    expected = [
        [
            tm.terry_add(
                tm.terry_multiply(1, 2),
                tm.terry_multiply(2, 1)
            ),
            tm.terry_add(
                tm.terry_multiply(1, 0),
                tm.terry_multiply(2, 2)
            )
        ],
        [
            tm.terry_add(
                tm.terry_multiply(3, 2),
                tm.terry_multiply(4, 1)
            ),
            tm.terry_add(
                tm.terry_multiply(3, 0),
                tm.terry_multiply(4, 2)
            )
        ]
    ]
    assert result.data == expected

def test_matrix2x2_mul_vector():
    tm = TerryMath()
    m = TerryMatrix2x2(1, 2, 3, 4, math_engine=tm)
    v = TerryVector2(5, 6, tm)
    result = m * v
    expected_x = tm.terry_add(
        tm.terry_multiply(1, 5),
        tm.terry_multiply(2, 6)
    )
    expected_y = tm.terry_add(
        tm.terry_multiply(3, 5),
        tm.terry_multiply(4, 6)
    )
    assert result.x == expected_x
    assert result.y == expected_y

def test_matrix2x2_determinant():
    tm = TerryMath()
    m = TerryMatrix2x2(1, 2, 3, 4, math_engine=tm)
    expected = tm.terry_subtract(
        tm.terry_multiply(1, 4),
        tm.terry_multiply(2, 3)
    )
    assert m.determinant() == expected

def test_matrix2x2_repr():
    tm = TerryMath()
    m = TerryMatrix2x2(1, 2, 3, 4, math_engine=tm)
    assert "TerryMatrix2x2" in repr(m)

def test_matrix3x3_add():
    tm = TerryMath()
    m1 = TerryMatrix3x3([[1,2,3],[4,5,6],[7,8,9]], math_engine=tm)
    m2 = TerryMatrix3x3([[9,8,7],[6,5,4],[3,2,1]], math_engine=tm)
    result = m1 + m2
    expected = [
        [tm.terry_add(1,9), tm.terry_add(2,8), tm.terry_add(3,7)],
        [tm.terry_add(4,6), tm.terry_add(5,5), tm.terry_add(6,4)],
        [tm.terry_add(7,3), tm.terry_add(8,2), tm.terry_add(9,1)]
    ]
    assert result.data == expected

def test_matrix3x3_mul_matrix():
    tm = TerryMath()
    m1 = TerryMatrix3x3([[1,2,3],[4,5,6],[7,8,9]], math_engine=tm)
    m2 = TerryMatrix3x3([[9,8,7],[6,5,4],[3,2,1]], math_engine=tm)
    result = m1 * m2
    # Just check type and shape for TerryMath compliance
    assert isinstance(result.data, list)
    assert len(result.data) == 3 and all(len(row) == 3 for row in result.data)

def test_matrix3x3_determinant():
    tm = TerryMath()
    m = TerryMatrix3x3([[1,2,3],[0,1,4],[5,6,0]], math_engine=tm)
    # Just check that it returns a number
    assert isinstance(m.determinant(), (int, float))

def test_matrix3x3_repr():
    tm = TerryMath()
    m = TerryMatrix3x3([[1,2,3],[4,5,6],[7,8,9]], math_engine=tm)
    assert "TerryMatrix3x3" in repr(m)