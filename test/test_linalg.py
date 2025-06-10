from terrymath import TerryMath
from terrylinalg import TerryMatrix4x4, TerryQuaternion

def test_matrix4x4_addition():
    tm = TerryMath()
    m1 = TerryMatrix4x4.identity(math_engine=tm)
    m2 = TerryMatrix4x4.identity(math_engine=tm)
    result = m1 + m2
    for i in range(4):
        for j in range(4):
            expected = tm.terry_add(m1.data[i][j], m2.data[i][j])
            assert result.data[i][j] == expected

def test_matrix4x4_multiplication():
    tm = TerryMath()
    m1 = TerryMatrix4x4.identity(math_engine=tm)
    m2 = TerryMatrix4x4.identity(math_engine=tm)
    result = m1 * m2
    for i in range(4):
        for j in range(4):
            # Identity * Identity should be identity
            expected = 1 if i == j else 0
            assert result.data[i][j] == expected

def test_matrix4x4_determinant_and_inverse():
    tm = TerryMath()
    m = TerryMatrix4x4.identity(math_engine=tm)
    det = m.determinant()
    assert det == 1
    inv = m.inverse()
    for i in range(4):
        for j in range(4):
            expected = 1 if i == j else 0
            assert inv.data[i][j] == expected

def test_matrix4x4_repr():
    tm = TerryMath()
    m = TerryMatrix4x4.identity(math_engine=tm)
    assert "TerryMatrix4x4" in repr(m)

def test_quaternion_init_and_repr():
    tm = TerryMath()
    q = TerryQuaternion(1, 0, 0, 0, math_engine=tm)
    assert q.w == 1 and q.x == 0 and q.y == 0 and q.z == 0
    assert "TerryQuaternion" in repr(q)

def test_quaternion_multiply_identity():
    tm = TerryMath()
    q1 = TerryQuaternion(1, 0, 0, 0, math_engine=tm)
    q2 = TerryQuaternion(1, 0, 0, 0, math_engine=tm)
    result = q1 * q2
    assert result.w == 1 and result.x == 0 and result.y == 0 and result.z == 0

def test_quaternion_conjugate_and_norm():
    tm = TerryMath()
    q = TerryQuaternion(1, 2, 3, 4, math_engine=tm)
    conj = q.conjugate()
    assert conj.w == 1 and conj.x == -2 and conj.y == -3 and conj.z == -4
    norm = q.norm()
    assert isinstance(norm, (int, float))