__all__ = ("is_prime",)


def is_prime(number: int) -> bool:
    """Определяет, является ли число простым.

    Example:
        >> is_prime(0):
        False
        >> is_prime(1):
        False
        >> is_prime(4):
        True
    """
    if number == 0 or number == 1:
        return False
    sqrt_number = int(number ** 0.5)
    for i in range(2, sqrt_number + 1):
        if number % i == 0:
            return False
    return True
