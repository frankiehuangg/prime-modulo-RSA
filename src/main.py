from tools import check_power_of_two
from Crypto.Util.number import getPrime, isPrime, long_to_bytes, bytes_to_long

import tonellishanks
import quadratic_residue


def case_one_modulo_four(
        ciphertext: int, 
        public_key_exponent: int, 
        prime: int, 
        debug_mode: bool
    ):
    """
    Computes modular square root iteratively with Tonelli-Shanks algorithm
    :param ciphertext: the ciphertext in integer
    :public_key_exponent: the public key exponent in the cryptosystem
    :prime: the prime number modulo
    :debug_mode: whether to print additional info
    """
    if (debug_mode):
        print(f"[DEBUG] public_key_exponent = {public_key_exponent}")

    if (public_key_exponent == 1):
        plaintext = long_to_bytes(ciphertext)
        print(plaintext)
    else:
        modular_square_root = tonellishanks.solve(ciphertext, prime)

        if (modular_square_root != None):
            for roots in modular_square_root:
                case_one_modulo_four(
                    roots,
                    public_key_exponent >> 1,
                    prime,
                    debug_mode
                )

def case_three_modulo_four(
        ciphertext: int, 
        public_key_exponent: int, 
        prime: int, 
        debug_mode: bool
    ):
    """
    Computes modular square root iteratively with Quadratic-Residue
    :param ciphertext: the ciphertext in integer
    :public_key_exponent: the public key exponent in the cryptosystem
    :prime: the prime number modulo
    :debug_mode: whether to print additional info
    """
    if (debug_mode):
        print(f"[DEBUG] public_key_exponent = {public_key_exponent}")

    if (public_key_exponent == 1):
        plaintext = long_to_bytes(ciphertext)
        print(plaintext)
    else:
        modular_square_root = quadratic_residue.solve(ciphertext, prime)

        if (modular_square_root != None):
            for roots in modular_square_root:
                case_one_modulo_four(
                    roots,
                    public_key_exponent >> 1,
                    prime,
                    debug_mode
                )


def main():
    is_valid = False

    # Select user choice
    user_choice_mode = 0
    while (not is_valid):
        print("Modular Square Root Calculator")
        print("1. Input the prime number manually")
        print("2. Randomly generate a prime number")

        user_choice_mode = int(input("Enter choice: "))
        if (user_choice_mode != 1 and user_choice_mode != 2):
            print("Please pick a valid input!")
        else:
            is_valid = True

    # Generate or input a prime number
    p = 0
    if (user_choice_mode == 1):
        while (not isPrime(p)):
            p = int(input("Enter your prime number: "))
    else:
        p = getPrime(1024)

    # Select DEBUG mode
    is_valid = False
    while (not is_valid):
        user_DEBUG_mode = input("Use DEBUG mode?[y/n]")

        if (user_DEBUG_mode == "y"):
            user_DEBUG_mode = True
            is_valid = True
        elif (user_DEBUG_mode == "n"):
            user_DEBUG_mode = False
            is_valid = True

    # Input message
    print(f"Message must be smaller than the prime p ({p})")
    message = input("Enter your message: ").encode("utf-8")

    # Check whether encryption is possible
    # message must be < p
    if (bytes_to_long(message) > p):
        print("[ERROR] message is larger than prime")
        print("Please pick another p value")
        exit()

    # Input public key exponent (e)
    public_key_exponent = 0
    while (not check_power_of_two(public_key_exponent)):
        print("Public key only supports in the form of 2^k")
        public_key_exponent = int(input("Enter the public key exponent: "))

    # Convert message to ciphertext
    ciphertext = pow(bytes_to_long(message), public_key_exponent, p)

    print(f"Ciphertext: {ciphertext}")

    if (not user_DEBUG_mode):
        print("\nPossible message values: ")

    if (p % 4 == 1):
        case_one_modulo_four(ciphertext, public_key_exponent, p, user_DEBUG_mode)
    else:
        case_three_modulo_four(ciphertext, public_key_exponent, p, user_DEBUG_mode)

main()
