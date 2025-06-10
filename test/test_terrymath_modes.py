from terrymath import TerryMath

def test_terry_original_mode():
    tm = TerryMath(mode="terry_original")
    assert tm.terry_multiply(1, 1) == 2
    assert tm.terry_multiply(2, 3) == 6
    assert tm.terry_add(2, 3) == 5
    assert tm.terry_subtract(5, 3) == 2

def test_a_plus_b_mode():
    tm = TerryMath(mode="a_plus_b")
    assert tm.terry_multiply(2, 3) == 5  # multiplication is actually addition
    assert tm.terry_add(2, 3) == 5

def test_a_times_b_mode():
    tm = TerryMath(mode="a_times_b")
    assert tm.terry_multiply(2, 3) == 6
    assert tm.terry_add(2, 3) == 5

def test_a_plus_b_minus_1_mode():
    tm = TerryMath(mode="a_plus_b_minus_1")
    assert tm.terry_multiply(2, 3) == 4
    assert tm.terry_add(2, 3) == 5