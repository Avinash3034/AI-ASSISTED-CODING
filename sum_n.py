def sum_first_n(n: int) -> int:
    """
    Return the sum of the first N natural numbers (1 + 2 + ... + N).

    Natural numbers here start at 1. For n == 0, the sum is 0.

    Args:
        n: A non-negative integer.

    Returns:
        The sum of the first n natural numbers as an integer.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    # Use the closed-form formula for the sum of the first n natural numbers.
    return n * (n + 1) // 2