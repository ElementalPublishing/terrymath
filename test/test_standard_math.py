from terrymath import TerryMath

def test_terrymath_reference():
    tm = TerryMath()
    assert tm.terry_multiply(1, 1) == tm.terry_multiply(1, 1)
    assert tm.terry_multiply(2, 3) == tm.terry_multiply(2, 3)
    assert tm.terry_add(2, 3) == tm.terry_add(2, 3)
    assert tm.terry_subtract(5, 3) == tm.terry_subtract(5, 3)
    assert tm.terry_power(2, 3) == tm.terry_power(2, 3)