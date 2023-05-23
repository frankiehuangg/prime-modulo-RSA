import random
from tools import inverse_modulo, lagendre_symbol

"""
THIS CODE WAS ORIGINALLY MADE BY ZeroBone
https://zerobone.net/blog/math/tonelli-shanks/

I SLIGHTLY MODIFIED THE CODE TO RETURN BOTH PAIR OF MODULAR
SQUARE ROOT.
"""

def randomize_b(p: int) -> int:
    """
    Choose a random b value
    p: odd prime modulo
    """
    b = 2
    while (lagendre_symbol(b, p) == 1):
        b = random.randrange(2, p)
    return b

def recursive(a: int, k: int, p: int, b: int, b_inverse: int) -> (int, int):
    """
    Computes the square root modulo prime p recursively
    :param a: the squared number value
    :param k: positive integer
    :param p: odd prime modulo
    :param b: an arbitrary non-square modulo p
    :param b_inverse: inverse of b modulo p
    :return: both pair of the square roots of a modulo p
    """
    m = (p - 1) >> k
    a_m = 1

    while (m % 2 == 0 and a_m == 1):
        m >>= 1
        k += 1
        a_m = pow(a, m, p)

    if (a_m == p - 1):
        b_power = 1 << (k - 1)
        b_power_half = 1 << (k - 2)
        a_next = (a * pow(b, b_power, p)) % p
        a_next_roots = recursive(a_next, k, p, b, b_inverse)

        for a_next_root in a_next_roots:
            a_root = a_next_root * pow(b_inverse, b_power_half, p)
            return (a_root % p, (p - a_root) % p)

    value = pow(a, (m + 1) >> 1, p)

    return (pow(value, 1, p), pow(p-value, 1, p))

def solve(a: int, p: int) -> (int, int):
    """
    Computes the square root modulo prime p
    :param a: the squared number value
    :param p: odd prime modulo
    :return: both pair of the square roots of a modulo p or None (if lagendre = -1)
    """
    if (lagendre_symbol(a, p) != 1):
        return None

    b = randomize_b(p)
    b_inverse = inverse_modulo(b, p)
    return recursive(a, 1, p, b, b_inverse)
