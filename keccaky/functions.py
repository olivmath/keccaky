from keccaky.algorithm import Keccak


def hash_it_bytes(data: bytes) -> bytes:
    """Calculates the Kecckak-256 hash

    Args:
        data (bytes): the input

    Returns:
        bytes: output hash
    """
    k = Keccak()
    return k.digest(data)


def hash_it(data: str) -> str:
    """
    # Calculates the Keccak-256 hash

    Args:
        data (str): The input string

    Returns:
        str: A hexadecimal string.

    Example:
        >>> Keccaky.hash_it("keccaky")
        'ff7e4a2e488ac0d8ed435b41979a0c1defeae30231dc5338a1b3a39c86adfd3c'
    """
    k = Keccak()
    return k.digest(data.encode()).hex()


def ethereum_hash(data: str) -> str:
    """
    # Calculates the Keccak-256 hash

    Args:
        data (str): The input string

    Returns:
        str: A hexadecimal string with '0x' in start

    Example:
        >>> Keccaky.ethereum_hash("keccaky")
        '0xff7e4a2e488ac0d8ed435b41979a0c1defeae30231dc5338a1b3a39c86adfd3c'
    """
    k = Keccak()
    return "0x" + k.digest(data.encode()).hex()
