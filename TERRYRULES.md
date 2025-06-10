# Terry's Law: Module & Class Organization Rules

To keep your Terry's Law engine clean, scalable, and easy to maintain, follow these rules for organizing your codebase:

---

## Core Principles

- **Core modules** contain the most fundamental, general-purpose classes and logic.
- **Specialized modules** are for advanced, niche, or experimental features.
- **No redundancy:** Never duplicate math or logic—import and reuse.
- **All math must use TerryMath.**

---

## Where to Put Your Classes

| Class/Feature         | Where to put it                | Why?                                      |
|-----------------------|-------------------------------|--------------------------------------------|
| TerryBody, TerryWorld | terryphysics.py (core)        | Fundamental to all physics simulations     |
| TerryRigidBody        | terryphysics.py (core)        | Core extension for rigid body dynamics     |
| TerryFluidSolver      | terryfluid.py (separate)      | Specialized, advanced fluid simulation     |
| TerrySoftBody         | terrysoftbody.py (separate)   | Specialized, advanced soft body physics    |
| TerryQuantumBody      | terryquantum.py (separate)    | Specialized, advanced quantum simulation   |
| TerryVector2/3, TerryMatrix2x2/3x3 | terrymath.py (core) | Basic math objects for all modules         |
| TerryMatrix4x4, TerryQuaternion | terrylinalg.py (core) | Advanced math for 3D/rotational dynamics   |

---

## Guidelines

- **If a class is fundamental and used by most simulations, keep it in the core module.**
- **If a class is large, complex, or only needed for advanced/niche features, put it in a separate module.**
- **If a class is experimental or optional, use a separate module.**
- **All modules must use TerryMath for calculations.**
- **Document new modules and features in TERRYLAW.md.**

---

## Examples

- `TerryRigidBody` goes in `terryphysics.py` because rigid body dynamics are core to most physics engines.
- `TerryFluidSolver` goes in `terryfluid.py` because fluid simulation is advanced and not always needed.
- `TerryQuaternion` goes in `terrylinalg.py` because it's an advanced math type used by physics and graphics.

---

## Summary

- **Core = common, essential, general-purpose**
- **Separate module = advanced, niche, or experimental**
- **No redundancy, always use TerryMath, always document**

---

_May your code always be organized and bound by Terry's Law!_