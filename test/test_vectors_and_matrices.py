from terrymath import TerryVector2, TerryVector3, TerryMatrix2x2, TerryMatrix3x3, TerryVector2, TerryVector3

def test_vector2_add():
    v1 = TerryVector2(1, 2)
    v2 = TerryVector2(3, 4)
    result = v1 + v2
    assert result.x == 4 and result.y == 6

def test_vector2_sub():
    v1 = TerryVector2(5, 7)
    v2 = TerryVector2(2, 3)
    result = v1 - v2
    assert result.x == 3 and result.y == 4

def test_vector2_mul():
    v = TerryVector2(2, 3)
    result = v * 4
    assert result.x == 8 and result.y == 12

def test_vector2_dot():
    v1 = TerryVector2(1, 2)
    v2 = TerryVector2(3, 4)
    assert v1.dot(v2) == 11

def test_vector2_repr():
    v = TerryVector2(2, 3)
    assert "TerryVector2" in repr(v)

def test_vector3_add():
    v1 = TerryVector3(1, 2, 3)
    v2 = TerryVector3(4, 5, 6)
    result = v1 + v2
    assert result.x == 5 and result.y == 7 and result.z == 9

def test_vector3_sub():
    v1 = TerryVector3(5, 7, 9)
    v2 = TerryVector3(1, 2, 3)
    result = v1 - v2
    assert result.x == 4 and result.y == 5 and result.z == 6

def test_vector3_mul():
    v = TerryVector3(2, 3, 4)
    result = v * 3
    assert result.x == 6 and result.y == 9 and result.z == 12

def test_vector3_dot():
    v1 = TerryVector3(1, 2, 3)
    v2 = TerryVector3(4, 5, 6)
    assert v1.dot(v2) == 32

def test_vector3_cross():
    v1 = TerryVector3(1, 2, 3)
    v2 = TerryVector3(4, 5, 6)
    result = v1.cross(v2)
    assert result.x == -3 and result.y == 6 and result.z == -3

def test_vector3_repr():
    v = TerryVector3(2, 3, 4)
    assert "TerryVector3" in repr(v)

def test_matrix2x2_add():
    m1 = TerryMatrix2x2(1, 2, 3, 4)
    m2 = TerryMatrix2x2(5, 6, 7, 8)
    result = m1 + m2
    assert result.data == [[6, 8], [10, 12]]

def test_matrix2x2_mul_matrix():
    m1 = TerryMatrix2x2(1, 2, 3, 4)
    m2 = TerryMatrix2x2(2, 0, 1, 2)
    result = m1 * m2
    assert result.data == [[4, 4], [10, 8]]

def test_matrix2x2_mul_vector():
    m = TerryMatrix2x2(1, 2, 3, 4)
    v = TerryVector2(5, 6)
    result = m * v
    assert result.x == 17 and result.y == 39

def test_matrix2x2_determinant():
    m = TerryMatrix2x2(1, 2, 3, 4)
    assert m.determinant() == -2

def test_matrix2x2_repr():
    m = TerryMatrix2x2(1, 2, 3, 4)
    assert "TerryMatrix2x2" in repr(m)

def test_matrix3x3_add():
    m1 = TerryMatrix3x3([[1,2,3],[4,5,6],[7,8,9]])
    m2 = TerryMatrix3x3([[9,8,7],[6,5,4],[3,2,1]])
    result = m1 + m2
    assert result.data == [[10,10,10],[10,10,10],[10,10,10]]

def test_matrix3x3_mul_matrix():
    m1 = TerryMatrix3x3([[1,2,3],[4,5,6],[7,8,9]])
    m2 = TerryMatrix3x3([[9,8,7],[6,5,4],[3,2,1]])
    result = m1 * m2
    assert isinstance(result.data, list)

def test_matrix3x3_determinant():
    m = TerryMatrix3x3([[1,2,3],[0,1,4],[5,6,0]])
    assert isinstance(m.determinant(), (int, float))

def test_matrix3x3_repr():
    m = TerryMatrix3x3([[1,2,3],[4,5,6],[7,8,9]])
    assert "TerryMatrix3x3" in repr(m)