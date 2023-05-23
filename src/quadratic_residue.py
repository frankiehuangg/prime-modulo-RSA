from tools import lagendre_symbol

def solve(a: int, p: int) -> (int, int):
    """
    Computes the square root modulo prime p when
    p == 3 mod 4
    :param a: the squared number value
    :param p: odd prime modulo
    :return: both pair of the square roots of a modulo p
    """
    if (lagendre_symbol(a, p) != 1):
        return None

    return (pow(a, (p + 1) // 4, p), pow(p - a, (p + 1) // 4, p))
