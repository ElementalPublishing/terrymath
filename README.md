![CI](https://github.com/ElementalPublishing/terrymath/actions/workflows/python-ci.yml/badge.svg)

# TerryMath & TerryPhysics

**TerryMath** is a modular, extensible mathematics and physics engine inspired by Terrence Howard’s math (“Terry’s Law”). Every calculation—arithmetic, geometry, linear algebra, and physics simulation—is powered by a customizable math engine, ensuring consistency and flexibility across all modules. TerryMath is designed for clarity, performance, and limitless expansion.

---

## Core Features

### TerryMath Engine
- **Custom Arithmetic Modes:** TerryMath supports multiple arithmetic rules (e.g., `a_times_b`, `a_plus_b`, `a_plus_b_minus_1`, `terry_original`).
- **Vectors & Matrices:** TerryVector2, TerryVector3, TerryMatrix2x2, TerryMatrix3x3, and advanced types in `terrylinalg.py` all use TerryMath.

### TerryPhysics
- **Newtonian Fundamentals:** Inertia, F=ma, action/reaction, gravity, momentum, energy, friction, and collisions—all powered by TerryMath.
- **Bodies & World:** TerryBody and TerryWorld classes simulate motion, forces, and interactions, always using Terry's Law.
- **TerryRigidBody:** Full rigid body with orientation, angular velocity, torque, inertia, sleeping, utility methods, and auto-sleep.
- **Universal Gravitation:** Terry's Law governs gravitational attraction between all bodies.

### TerryGeometry
- **Primitives:** Points, lines, rays, planes, spheres, boxes, triangles, cubes, and quads.
- **Intersection & Containment:** All geometric tests and mesh generation use TerryMath.

### TerryLinalg
- **Advanced Linear Algebra:** 4x4 matrices, quaternions, interpolation, and rotation—all using TerryMath.

### TerryShader
- **Procedural Graphics:** TerryMath powers all shader logic, patterns, and procedural effects.

---

## TerryRigidBody: Core Features

1. **Collision Shape Support** (reference, ready for future expansion)
2. **Mass & Inertia Tensor** (scalar for now, matrix later)
3. **Linear & Angular Motion** (position, velocity, orientation, angular velocity)
4. **Force & Torque Application** (including off-center force application)
5. **Energy & Momentum** (linear and angular)
6. **State Integration** (linear and angular, with TerryMath)
7. **Sleeping** (performance optimization, with auto-sleep logic)
8. **Utility Methods** (reset, set/get state, etc.)

---

## Project Structure

```
terrymath/
├── terrymath.py
├── terrylinalg.py
├── terrygeometry.py
├── terryphysics.py
├── tests/
│   └── test_terrymath.py
├── README.md
├── TERRYLAW.md
├── TERRYRULES.md
├── requirements.txt
├── .github/
│   └── workflows/
│       └── python-ci.yml
```

---

## CI/CD Setup

This project uses **GitHub Actions** for continuous integration:

- On every push or pull request to `main`, the workflow:
  - Checks out the code
  - Sets up Python 3.11
  - Installs dependencies from `requirements.txt` (if present)
  - Runs all tests in the `tests/` directory using `unittest`

**Sample workflow file:**  
`.github/workflows/python-ci.yml`
```yaml
name: TerryMath CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Run tests
      run: |
        python -m unittest discover -s tests -p "test_*.py"
```

---

## Contributing

- All new modules must use TerryMath for their core logic.
- Extensions to new domains (AI, thermodynamics, quantum, etc.) must honor Terry's Law.
- Document all Terry-based logic and innovations in TERRYLAW.md and TERRYRULES.md.

---

## The Spirit of Terry's Law

- **All modules, all features, all realms—are bound by Terry's Law.**
- **No calculation escapes its reach.**
- **Terry's Law is the foundation and the future of this engine.**

---

_May all your code be bound by Terry's Law._