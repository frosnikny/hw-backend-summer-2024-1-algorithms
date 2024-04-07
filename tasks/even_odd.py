__all__ = ("even_odd",)


def even_odd(numbers: list[int]) -> float:
    """Определяет отношение суммы четных элементов списка
    к сумме нечетных.

    Example:
        >> even_odd([1, 2, 3, 4, 5])
        0.6667
    """
    sum_even = sum(i for i in numbers if i % 2 == 0)
    sum_odd = sum(i for i in numbers if i % 2 != 0)
    if sum_odd == 0:
        return 0
    return sum_even / sum_odd
