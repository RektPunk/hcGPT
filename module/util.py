import hashlib


def random_hash(text: str, time: str) -> str:
    """
    Make random hash string
    Args:
        text (str): input string
        time (str): timestamp
    Returns:
        str: hash value
    """
    hash_value = hashlib.sha256()
    hash_value.update(text.encode("utf-8"))
    hash_value.update(time.encode("utf-8"))
    return hash_value.digest()
