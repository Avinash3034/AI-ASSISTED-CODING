from sum_n import sum_first_n


def run_tests() -> None:
    # Basic correctness tests
    assert sum_first_n(0) == 0
    assert sum_first_n(1) == 1
    assert sum_first_n(2) == 3
    assert sum_first_n(5) == 15
    assert sum_first_n(10) == 55

    # Large input test
    assert sum_first_n(1_000_000) == 500_000 * 1_000_001

    # Error cases
    try:
        sum_first_n(-1)
        raise AssertionError("Expected ValueError for negative n")
    except ValueError:
        pass

    try:
        sum_first_n(3.5)  # type: ignore[arg-type]
        raise AssertionError("Expected TypeError for non-integer n")
    except TypeError:
        pass

    # Show example outputs
    print("sum_first_n(0) =", sum_first_n(0))
    print("sum_first_n(1) =", sum_first_n(1))
    print("sum_first_n(5) =", sum_first_n(5))
    print("sum_first_n(10) =", sum_first_n(10))

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()