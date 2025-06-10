from terrymath import TerryMath

def test_compare_terrymath_and_standard():
    tm = TerryMath(mode="terry_original")
    # Terry's Law vs standard math
    assert tm.terry_multiply(1, 1) != 1  # Terry's Law: 1*1=2, standard: 1
    assert tm.terry_multiply(2, 3) == 2 * 3  # Both 6 in this mode
    assert tm.terry_add(2, 3) == 2 + 3      # Both 5
    # Show where they diverge
    tm_plus = TerryMath(mode="a_plus_b")
    assert tm_plus.terry_multiply(2, 3) != 2 * 3  # 5 vs 6