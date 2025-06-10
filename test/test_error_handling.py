import pytest
from terrymath import TerryMath, TerryVector2, TerryVector3, TerryMatrix2x2, TerryMatrix3x3

def test_invalid_terrymath_mode():
    with pytest.raises(ValueError):
        TerryMath(mode="not_a_real_mode")

def test_vector2_dot_invalid_type():
    v = TerryVector2(1, 2)
    with pytest.raises(TypeError):
        v.dot("not a vector")

def test_vector3_dot_invalid_type():
    v = TerryVector3(1, 2, 3)
    with pytest.raises(TypeError):
        v.dot([1, 2, 3])

def test_vector3_cross_invalid_type():
    v = TerryVector3(1, 2, 3)
    with pytest.raises(TypeError):
        v.cross(123)

def test_vector2_add_invalid_type():
    v = TerryVector2(1, 2)
    with pytest.raises(TypeError):
        _ = v + 5

def test_vector2_sub_invalid_type():
    v = TerryVector2(1, 2)
    with pytest.raises(TypeError):
        _ = v - "a"

def test_vector2_mul_invalid_type():
    v = TerryVector2(1, 2)
    with pytest.raises(TypeError):
        _ = v * "b"

def test_vector2_repr():
    v = TerryVector2(1, 2)
    assert "TerryVector2" in repr(v)

def test_vector3_repr():
    v = TerryVector3(1, 2, 3)
    assert "TerryVector3" in repr(v)

def test_matrix2x2_add_invalid_type():
    m = TerryMatrix2x2(1, 2, 3, 4)
    with pytest.raises(TypeError):
        _ = m + 5

def test_matrix2x2_mul_invalid_type():
    m = TerryMatrix2x2(1, 2, 3, 4)
    with pytest.raises(TypeError):
        _ = m * "not a matrix or vector"

def test_matrix2x2_inverse_singular():
    m = TerryMatrix2x2(1, 2, 2, 4)  # determinant is 0
    with pytest.raises(ValueError):
        m.inverse()

def test_matrix3x3_add_invalid_type():
    m = TerryMatrix3x3([[1,2,3],[4,5,6],[7,8,9]])
    with pytest.raises(TypeError):
        _ = m + 5

def test_matrix3x3_mul_invalid_type():
    m = TerryMatrix3x3([[1,2,3],[4,5,6],[7,8,9]])
    with pytest.raises(TypeError):
        _ = m * "not a matrix"

def test_matrix3x3_inverse_singular():
    m = TerryMatrix3x3([[1,2,3],[2,4,6],[3,6,9]])  # determinant is 0
    with pytest.raises(ValueError):
        m.inverse()

def test_matrix3x3_inverse():
    m = TerryMatrix3x3([[1,2,3],[0,1,4],[5,6,0]])
    inv = m.inverse()
    assert isinstance(inv, TerryMatrix3x3)

def test_matrix2x2_repr():
    m = TerryMatrix2x2(1, 2, 3, 4)
    assert "TerryMatrix2x2" in repr(m)

def test_matrix3x3_repr():
    m = TerryMatrix3x3([[1,2,3],[4,5,6],[7,8,9]])
    assert "TerryMatrix3x3" in repr(m)