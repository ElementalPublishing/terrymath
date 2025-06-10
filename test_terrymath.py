import math
import pytest
from terrymath import TerryMath

@pytest.mark.parametrize("mode, expected", [
    ("a_plus_b_minus_1", 2),
    ("a_plus_b", 2),
    ("a_times_b", 1),
    ("terry_original", 2),
])
def test_one_times_one(mode, expected):
    tm = TerryMath(mode=mode)
    assert tm.terry_multiply(1, 1) == expected

@pytest.mark.parametrize("mode, a, b, expected", [
    ("a_plus_b_minus_1", 2, 3, 4),
    ("a_plus_b", 2, 3, 5),
    ("a_times_b", 2, 3, 6),
    ("terry_original", 2, 3, 6),
])
def test_two_times_three(mode, a, b, expected):
    tm = TerryMath(mode=mode)
    assert tm.terry_multiply(a, b) == expected

@pytest.mark.parametrize("mode", ["a_plus_b_minus_1", "a_plus_b", "a_times_b", "terry_original"])
@pytest.mark.parametrize("a,b", [(1,2), (2,3), (5,7), (0,4), (-1,3)])
def test_commutativity(mode, a, b):
    tm = TerryMath(mode=mode)
    assert tm.terry_multiply(a, b) == tm.terry_multiply(b, a)

@pytest.mark.parametrize("mode", ["a_plus_b_minus_1", "a_plus_b", "a_times_b", "terry_original"])
@pytest.mark.parametrize("a,b,c", [(1,2,3), (2,3,4), (0,1,2), (5,0,1)])
def test_associativity(mode, a, b, c):
    tm = TerryMath(mode=mode)
    left = tm.terry_multiply(tm.terry_multiply(a, b), c)
    right = tm.terry_multiply(a, tm.terry_multiply(b, c))
    if mode == "a_times_b":
        assert left == right
    else:
        print(f"Associativity ({mode}): ({a}*{b})*{c}={left}, {a}*({b}*{c})={right}")

@pytest.mark.parametrize("mode", ["a_plus_b_minus_1", "a_plus_b", "a_times_b", "terry_original"])
@pytest.mark.parametrize("a,b,c", [(1,2,3), (2,3,4), (0,1,2), (5,0,1)])
def test_distributivity(mode, a, b, c):
    tm = TerryMath(mode=mode)
    left = tm.terry_multiply(a, tm.terry_add(b, c))
    right = tm.terry_add(tm.terry_multiply(a, b), tm.terry_multiply(a, c))
    if mode == "a_times_b":
        assert left == right
    else:
        print(f"Distributivity ({mode}): {a}*({b}+{c})={left}, {a}*{b}+{a}*{c}={right}")

@pytest.mark.parametrize("mode", ["a_plus_b_minus_1", "a_plus_b", "a_times_b", "terry_original"])
def test_identity_property(mode):
    tm = TerryMath(mode=mode)
    for i in range(-3, 6):
        left = tm.terry_multiply(1, i)
        right = tm.terry_multiply(i, 1)
        if mode == "a_times_b":
            assert left == i and right == i
        else:
            print(f"Identity ({mode}): 1*{i}={left}, {i}*1={right}")

@pytest.mark.parametrize("mode", ["a_plus_b_minus_1", "a_plus_b", "a_times_b", "terry_original"])
def test_zero_property(mode):
    tm = TerryMath(mode=mode)
    for i in range(-3, 6):
        left = tm.terry_multiply(0, i)
        right = tm.terry_multiply(i, 0)
        if mode == "a_times_b":
            assert left == 0 and right == 0
        else:
            print(f"Zero ({mode}): 0*{i}={left}, {i}*0={right}")

@pytest.mark.parametrize("a,b", [(2,3), (3,2), (4,0), (1,5), (5,1)])
def test_terry_power_vs_standard(a, b):
    tm_std = TerryMath(mode="a_times_b")
    tm_terry = TerryMath(mode="a_plus_b_minus_1")
    terry_result = tm_terry.terry_power(a, b)
    std_result = tm_std.terry_power(a, b)
    print(f"Terry power {a}^{b}={terry_result}, Standard {a}^{b}={std_result}")

@pytest.mark.parametrize("mode", ["a_plus_b_minus_1", "a_plus_b", "a_times_b", "terry_original"])
@pytest.mark.parametrize("a,b", [(1,1), (2,2), (3,3), (4,4), (5,5)])
def test_symmetry(mode, a, b):
    tm = TerryMath(mode=mode)
    assert tm.terry_multiply(a, b) == tm.terry_multiply(b, a)

# a. Algebraic Structure: Check group/ring/field axioms
@pytest.mark.parametrize("mode", ["a_plus_b_minus_1", "a_plus_b", "a_times_b", "terry_original"])
def test_group_ring_field_axioms(mode):
    tm = TerryMath(mode=mode)
    # Closure: a*b in Z for a,b in Z
    for a in range(-5, 6):
        for b in range(-5, 6):
            result = tm.terry_multiply(a, b)
            assert isinstance(result, int)
    # Identity: is there an e such that a*e = e*a = a?
    identity_found = False
    for e in range(-5, 6):
        if all(tm.terry_multiply(a, e) == a and tm.terry_multiply(e, a) == a for a in range(-5, 6)):
            identity_found = True
            print(f"Mode {mode}: Identity element is {e}")
            break
    if mode == "a_times_b":
        assert identity_found
    else:
        print(f"Mode {mode}: Identity found? {identity_found}")
    # Inverses: For each a, is there b such that a*b = identity?
    # (Skip for brevity, but you can add this check.)

# b. Solving equations: x^2 = 1 and x^2 = 2
@pytest.mark.parametrize("mode", ["a_plus_b_minus_1", "a_plus_b", "a_times_b", "terry_original"])
def test_solve_x_squared_eq_1_and_2(mode):
    tm = TerryMath(mode=mode)
    for x in range(-10, 11):
        sq = tm.terry_multiply(x, x)
        if sq == 1:
            print(f"Mode {mode}: x^2=1 has solution x={x}")
        if sq == 2:
            print(f"Mode {mode}: x^2=2 has solution x={x}")

# c. Number theory: Primality and factorization
@pytest.mark.parametrize("mode", ["a_plus_b_minus_1", "a_plus_b", "a_times_b", "terry_original"])
def test_primality_and_factorization(mode):
    tm = TerryMath(mode=mode)
    for n in range(2, 20):
        factors = []
        for a in range(1, n+1):
            for b in range(1, n+1):
                if tm.terry_multiply(a, b) == n:
                    factors.append((a, b))
        if len(factors) == 2:  # Only (1, n) and (n, 1)
            print(f"Mode {mode}: {n} is prime (by Terry multiplication)")
        else:
            print(f"Mode {mode}: {n} factors: {factors}")

# d. Geometry/Physics: Vector scaling (simple 2D vector)
@pytest.mark.parametrize("mode", ["a_plus_b_minus_1", "a_plus_b", "a_times_b", "terry_original"])
def test_vector_scaling(mode):
    tm = TerryMath(mode=mode)
    vector = (3, 4)
    for scalar in range(-2, 3):
        scaled = (tm.terry_multiply(scalar, vector[0]), tm.terry_multiply(scalar, vector[1]))
        print(f"Mode {mode}: {scalar} * {vector} = {scaled}")

# --- Set Theory Foundations ---

@pytest.mark.parametrize("mode", ["a_plus_b_minus_1", "a_plus_b", "a_times_b", "terry_original"])
def test_set_cardinality_union_intersection(mode):
    tm = TerryMath(mode=mode)
    # Model sets as finite lists
    A = set([1, 2, 3])
    B = set([3, 4, 5])
    union = A | B
    intersection = A & B
    # Standard cardinality
    std_union = len(union)
    std_intersection = len(intersection)
    # Terry cardinality: use terry_add or terry_multiply for union/intersection
    terry_union = tm.terry_add(len(A), len(B)) - len(intersection)  # Inclusion-Exclusion
    terry_intersection = len(intersection)
    print(f"Mode {mode}: |A|={len(A)}, |B|={len(B)}, |A∪B|={std_union}, Terry union={terry_union}")
    print(f"Mode {mode}: |A∩B|={std_intersection}, Terry intersection={terry_intersection}")

# --- Model Goldbach's Conjecture (every even >2 is sum of two primes) ---
@pytest.mark.parametrize("mode", ["a_plus_b_minus_1", "a_plus_b", "a_times_b", "terry_original"])
def test_goldbach_conjecture(mode):
    tm = TerryMath(mode=mode)
    # Use Terry's multiplication to define "prime"
    def is_terry_prime(n):
        count = 0
        for a in range(1, n+1):
            for b in range(1, n+1):
                if tm.terry_multiply(a, b) == n:
                    count += 1
        return count == 2  # Only (1, n) and (n, 1)
    # Test for even numbers 4 to 20
    for even in range(4, 21, 2):
        found = False
        for p1 in range(2, even):
            for p2 in range(2, even):
                if is_terry_prime(p1) and is_terry_prime(p2) and tm.terry_add(p1, p2) == even:
                    found = True
                    print(f"Mode {mode}: {even} = {p1} + {p2} (Terry primes)")
                    break
            if found:
                break
        if not found:
            print(f"Mode {mode}: Goldbach fails for {even}")

# --- Model Collatz Conjecture (using Terry multiplication) ---
@pytest.mark.parametrize("mode", ["a_plus_b_minus_1", "a_plus_b", "a_times_b", "terry_original"])
def test_collatz_conjecture(mode):
    tm = TerryMath(mode=mode)
    def terry_collatz(n):
        steps = 0
        seen = set()
        while n != 1 and n not in seen and steps < 1000:
            seen.add(n)
            if n % 2 == 0:
                n = n // 2
            else:
                n = tm.terry_add(tm.terry_multiply(3, n), 1)
            steps += 1
        return n == 1
    for start in range(2, 20):
        result = terry_collatz(start)
        print(f"Mode {mode}: Collatz({start}) reaches 1? {result}")

# --- Model Twin Prime Conjecture (using Terry primes) ---
@pytest.mark.parametrize("mode", ["a_plus_b_minus_1", "a_plus_b", "a_times_b", "terry_original"])
def test_twin_prime_conjecture(mode):
    tm = TerryMath(mode=mode)
    def is_terry_prime(n):
        count = 0
        for a in range(1, n+1):
            for b in range(1, n+1):
                if tm.terry_multiply(a, b) == n:
                    count += 1
        return count == 2
    last_prime = None
    for n in range(2, 50):
        if is_terry_prime(n):
            if last_prime is not None and n - last_prime == 2:
                print(f"Mode {mode}: Twin Terry primes: {last_prime}, {n}")
            last_prime = n

# --- Terry Factorial ---
def terry_factorial(tm, n):
    result = 1
    for i in range(1, n+1):
        result = tm.terry_multiply(result, i)
    return result

# --- Terry Binomial Coefficient ---
def terry_binom(tm, n, k):
    # Terry's version of n! / (k! * (n-k)!)
    num = terry_factorial(tm, n)
    denom = tm.terry_multiply(terry_factorial(tm, k), terry_factorial(tm, n-k))
    # Avoid division by zero or negative
    if denom == 0:
        return None
    return num // denom if isinstance(num, int) and isinstance(denom, int) else None

@pytest.mark.parametrize("mode", ["a_plus_b_minus_1", "a_plus_b", "a_times_b", "terry_original"])
def test_terry_factorial_and_binomial(mode):
    tm = TerryMath(mode=mode)
    for n in range(0, 7):
        tfact = terry_factorial(tm, n)
        sfact = math.factorial(n)
        print(f"Mode {mode}: {n}! Terry={tfact}, Standard={sfact}")
        for k in range(0, n+1):
            tbinom = terry_binom(tm, n, k)
            sbinom = math.comb(n, k)
            print(f"Mode {mode}: C({n},{k}) Terry={tbinom}, Standard={sbinom}")

# --- Terry Cartesian Product Cardinality ---
@pytest.mark.parametrize("mode", ["a_plus_b_minus_1", "a_plus_b", "a_times_b", "terry_original"])
def test_cartesian_product_cardinality(mode):
    tm = TerryMath(mode=mode)
    sets = [
        (set([1,2]), set([3,4,5])),
        (set([1]), set([2])),
        (set([1,2,3]), set([4,5]))
    ]
    for A, B in sets:
        std = len(A) * len(B)
        terry = tm.terry_multiply(len(A), len(B))
        print(f"Mode {mode}: |A|={len(A)}, |B|={len(B)}, |A×B| std={std}, Terry={terry}")

# --- Terry Subset Counting (Power Set) ---
@pytest.mark.parametrize("mode", ["a_plus_b_minus_1", "a_plus_b", "a_times_b", "terry_original"])
def test_terry_power_set_count(mode):
    tm = TerryMath(mode=mode)
    for n in range(0, 6):
        std = 2 ** n
        terry = tm.terry_power(2, n)
        print(f"Mode {mode}: Power set of {n} elements: Terry={terry}, Standard={std}")

# --- Terry Inclusion-Exclusion Principle ---
@pytest.mark.parametrize("mode", ["a_plus_b_minus_1", "a_plus_b", "a_times_b", "terry_original"])
def test_terry_inclusion_exclusion(mode):
    tm = TerryMath(mode=mode)
    # |A ∪ B| = |A| + |B| - |A ∩ B|
    A = set(range(1, 5))
    B = set(range(3, 8))
    std_union = len(A | B)
    std_inter = len(A & B)
    terry_union = tm.terry_add(len(A), len(B)) - len(A & B)
    print(f"Mode {mode}: |A|={len(A)}, |B|={len(B)}, |A∩B|={std_inter}, |A∪B| Terry={terry_union}, Standard={std_union}")

# --- Terry Multiset/Combination Counting ---
@pytest.mark.parametrize("mode", ["a_plus_b_minus_1", "a_plus_b", "a_times_b", "terry_original"])
def test_terry_multiset_combinations(mode):
    tm = TerryMath(mode=mode)
    # Number of multisets of size k from n types: C(n+k-1, k)
    for n in range(1, 5):
        for k in range(0, 4):
            tbinom = terry_binom(tm, n+k-1, k)
            sbinom = math.comb(n+k-1, k)
            print(f"Mode {mode}: Multisets of size {k} from {n} types: Terry={tbinom}, Standard={sbinom}")

# --- Add more set theory or conjecture tests as you wish! ---