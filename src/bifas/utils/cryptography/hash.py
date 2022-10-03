import hashlib

from bifas.utils.data_structure.binary import Binary

def sha256(
    x:Binary=Binary(x=0),
) -> Binary:
    """
    Using SHA256 to hash Binary to fixed length of 256 bits Binary.

    Parameters
    ----------
    x : Binary, default Binary(x=0)

    Returns
    -------
    Binary
        The hash value stored as Binary.

    See Also
    --------
    bifas.utils.data_structure.binary.Binary

    Examples
    --------
    >>> from bifas.utils.data_structure.binary import Binary
    >>> from bifas.utils.cryptography.hash import sha256
    >>> question = b"Blockchain International Financial Assets System (BIFAS)"
    >>> answer = "55affbc3b2c2b989f32e3b6cae1ca4bd154a7347adcf380297b484e9d387f5c0"
    >>> answer == sha256(Binary(x=question)).get_x(data_type="str")
    True
    """
    return Binary(
        hashlib.sha256(
            x.get_x(data_type="bytes")
        ).digest()
    )