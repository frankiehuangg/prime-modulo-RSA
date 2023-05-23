def inverse_modulo(a: int, n: int) -> int:
    """
    Calculates the inverse modulo of a modulo n
    :param a: integer 0 < a < n
    :param n: modulo
    :return: the inverse modulo of a modulo n
    """
    return pow(a, -1, n)

def lagendre_symbol(a: int, p: int) -> int:
    """
    Checks the lagendre symbol of a in modulo p
    :param a: integer 0 < a < p
    :param p: prime modulo
    :return: the lagendre symbol of a in modulo p
    """
    return pow(a, (p - 1) // 2, p)

def check_power_of_two(a: int) -> bool:
    """
    Checks if a is a power of 2
    :param a: integer to check
    :return: boolean whether a is a power of 2
    """
    return (a > 0) and ((a & (a - 1)) == 0)
