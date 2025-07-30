"""Generate secret for JWT"""

# -- Imports

import secrets
import string

# --


def generate_secret(length: int = 64) -> str:
    """
    Generate a secure random secret string.

    Args:
        length (int): Length of the secret string. Default is 64.

    Returns:
        str: A securely generated random secret.
    """
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))


if __name__ == "__main__":
    print(generate_secret())
