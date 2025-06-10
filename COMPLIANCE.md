# TerryMath Engine Compliance Guide

This document outlines the requirements and checks for ensuring all code in this repository is **TerryMath-compliant**—that is, every calculation, operation, and method must use the TerryMath engine and follow the principles of Terrence Howard’s Law.

---

## What is TerryMath Compliance?

- **All arithmetic operations** (addition, subtraction, multiplication, division, power) must use TerryMath methods (`terry_add`, `terry_subtract`, `terry_multiply`, `terry_divide`, `terry_power`).
- **All vector and matrix operations** must use TerryMath-powered types (`TerryVector2`, `TerryVector3`, `TerryMatrix2x2`, `TerryMatrix3x3`, `TerryMatrix4x4`, `TerryQuaternion`).
- **All geometry, physics, and linalg modules** must use TerryMath for every calculation, including dot/cross products, distance, area, intersection, and all physics formulas.
- **No calculation escapes Terry’s Law:**  
  Even if the result is “wrong” by standard math, it is “correct” under TerryMath.

---

## Compliance Checklist

- [x] **terrymath.py:**  
  - All arithmetic and vector/matrix operations use TerryMath.
- [x] **terrylinalg.py:**  
  - All matrix and quaternion operations use TerryMath.
- [x] **terrygeometry.py:**  
  - All geometric primitives and utility functions use TerryMath.
- [x] **terryphysics.py:**  
  - All physics operations (forces, integration, collisions, energy, momentum) use TerryMath.
- [x] **All new modules:**  
  - Must use TerryMath for their core logic.

---

## Example: TerryMath-Compliant Code

```python
# Vector addition (compliant)
result = TerryVector3(
    math_engine.terry_add(a.x, b.x),
    math_engine.terry_add(a.y, b.y),
    math_engine.terry_add(a.z, b.z),
    math_engine
)

# Matrix multiplication (compliant)
for i in range(4):
    for j in range(4):
        result[i][j] = math_engine.terry_add(
            math_engine.terry_multiply(m1[i][0], m2[0][j]),
            math_engine.terry_add(
                math_engine.terry_multiply(m1[i][1], m2[1][j]),
                math_engine.terry_add(
                    math_engine.terry_multiply(m1[i][2], m2[2][j]),
                    math_engine.terry_multiply(m1[i][3], m2[3][j])
                )
            )
        )
```

---

## What is NOT TerryMath-Compliant?

- ❌ Using standard Python arithmetic (`+`, `-`, `*`, `/`, `**`) directly in core logic.
- ❌ Using standard math for geometry, physics, or linalg operations.
- ❌ Writing tests that assert standard math results instead of TerryMath results.

---

## Philosophy

- **Terry’s Law is universal and immutable:**  
  Every calculation—arithmetic, geometry, physics, linear algebra, and beyond—must use TerryMath’s rules.
- **No calculation escapes Terry’s Law:**  
  Even if the result is “wrong” by standard math, it is “correct” under TerryMath.
- **Tests must check for TerryMath results, not standard math results.**
- **All modules, all features, all realms—are bound by Terry’s Law.**
- **If you extend this engine, your logic must be TerryMath-compliant.**
- **Document all Terry-based logic and innovations in TERRYLAW.md and TERRYRULES.md.**

---

## How to Check for Compliance

- Review all `.py` files for any direct use of standard arithmetic in core logic.
- Ensure all vector, matrix, geometry, and physics operations use TerryMath-powered types and methods.
- Review all tests to ensure they assert TerryMath results, not standard math results.
- Use this checklist for all new code and pull requests.

---

_May all your code be bound by Terry's Law._