# TerryMath Test Philosophy

## Purpose

These tests exist to **prove that every calculation in this project follows Terry’s Law** (Terrence Howard’s math), not standard arithmetic.  
All math operations—addition, multiplication, subtraction, etc.—must use the TerryMath engine and its modes.

## What We Test

- **TerryMath Modes:**  
  We verify that each mode (`terry_original`, `a_plus_b`, `a_times_b`, `a_plus_b_minus_1`) produces the expected results for all core operations.
- **Consistency:**  
  All calculations in vectors, matrices, and physics modules are bound by Terry’s Law.
- **Edge Cases & Error Handling:**  
  We test not just typical cases, but also edge cases and error handling to ensure robustness.

## Why This Matters

- **Consistency:**  
  Mixing standard math and TerryMath would defeat the purpose of the engine and produce inconsistent results.
- **Demonstration:**  
  The tests show, with concrete examples, how Terry’s Law changes the outcome of basic and advanced math operations.
- **Extendability:**  
  By enforcing TerryMath everywhere, any new module or feature will automatically follow Terry’s Law.

## Example: Terry’s Law in Action

```python
from terrymath import TerryMath

tm = TerryMath(mode="terry_original")
assert tm.terry_multiply(1, 1) == 2  # Terry's Law: 1 x 1 = 2
assert tm.terry_add(2, 3) == 5