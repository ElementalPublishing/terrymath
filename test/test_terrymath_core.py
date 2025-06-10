import pytest
from terrymath import TerryMath

@pytest.mark.parametrize("mode, a, b, expected", [
    ("terry_original", 1, 1, 2),
    ("a_plus_b", 1, 1, 2),
    ("a_times_b", 1, 1, 1),
    ("a_plus_b_minus_1", 1, 1, 1),
    ("terry_original", 2, 3, 6),
    ("a_plus_b", 2, 3, 5),
    ("a_times_b", 2, 3, 6),
    ("a_plus_b_minus_1", 2, 3, 4),
])
def test_terry_multiply(mode, a, b, expected):
    tm = TerryMath(mode=mode)
    assert tm.terry_multiply(a, b) == expected

@pytest.mark.parametrize("mode", ["terry_original", "a_plus_b", "a_times_b", "a_plus_b_minus_1"])
def test_terry_add(mode):
    tm = TerryMath(mode=mode)
    assert tm.terry_add(2, 3) == 5

@pytest.mark.parametrize("mode", ["terry_original", "a_plus_b", "a_times_b", "a_plus_b_minus_1"])
def test_terry_subtract(mode):
    tm = TerryMath(mode=mode)
    assert tm.terry_subtract(5, 3) == 2

@pytest.mark.parametrize("mode", ["terry_original", "a_plus_b", "a_times_b", "a_plus_b_minus_1"])
def test_terry_divide(mode):
    tm = TerryMath(mode=mode)
    assert tm.terry_divide(6, 2) == 3

@pytest.mark.parametrize("mode", ["terry_original", "a_plus_b", "a_times_b", "a_plus_b_minus_1"])
def test_terry_power(mode):
    tm = TerryMath(mode=mode)
    # Terry power for 2^3
    result = tm.terry_power(2, 3)
    if mode == "a_times_b":
        assert result == 8
    elif mode == "a_plus_b":
        assert result == 6
    elif mode == "a_plus_b_minus_1":
        assert result == 4
    elif mode == "terry_original":
        assert result == 8

def test_terrymath_modes_list():
    modes = TerryMath.list_modes()
    assert "terry_original" in modes
    assert "a_times_b" in modes
    assert "a_plus_b" in modes
    assert "a_plus_b_minus_1" in modes

# Add more focused tests for edge cases as needed