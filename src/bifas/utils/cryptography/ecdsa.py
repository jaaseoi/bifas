from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256
from Crypto.Signature import DSS
from bifas.utils.data_structure.binary import Binary
import os

MODE = "fips-186-3"

class ECDSA:
    """
    DSA and ECDSA are U.S. federal standards for digital signatures, specified in FIPS PUB 186-4.

    Parameters
    ----------
    passphrase:Binary, default None,
        If passphrase == None, random generate 256 bit string.
    Examples
    --------
    >>> ecdsa = ECDSA(
        passphrase=Binary(
            x="BIFAS",
            data_format="utf-8",
        )
    )
    >>> self.assertEqual(b"\x42\x49\x46\x41\x53", ecdsa.passphrase.get_x(data_format="bytes"))
    True
    >>> message = Binary(
        x="This is the receipt. Blockchain International Financial Asset System",
        data_format="utf-8",
    )
    >>> message = Binary(
        x="This is the receipt. Blockchain International Financial Asset System",
        data_format="utf-8",
    )
    >>> self.assertEqual(
        ecdsa.verify(
            public_key=ecdsa.public_key,
            message=message,
            signature=ecdsa.sign(
                message=message,
            ),
        ),
        True,
    )
    True
    """
    def __init__(
        self,
        passphrase:Binary=None,
    ) -> None:
        self.passphrase, self.private_key, self.public_key, self.address = None, None, None, None
        if ((passphrase == None) or (type(passphrase) != Binary)):
            self.passphrase = Binary(
                x=os.urandom(32),   # 256 bits
                data_format="bytes",
            )
        else:
            self.passphrase = passphrase
        __ecc_keys = ECC.construct(
            curve="P-256",
            d=int(
                SHA256.new(
                    data=self.passphrase.get_x(
                        data_format="bytes",
                    ),
                ).hexdigest(),
                base=16,
            ),
        )
        self.private_key = Binary(
            x=__ecc_keys.export_key(format="PEM"),
            data_format="ascii",
        )
        self.public_key = Binary(
            x=__ecc_keys.public_key().export_key(format="PEM"),
            data_format="ascii",
        )
        pass

    def sign(
        self,
        message:Binary=None,
    ) -> Binary:
        return Binary(
            DSS.new(
                key=ECC.import_key(self.private_key.get_x(data_format="ascii")),
                mode=MODE,
            ).sign(
                msg_hash=SHA256.new(message.get_x(data_format="bytes")),
            ),
            data_format="bytes",
        )

    def verify(
        self,
        public_key:Binary,
        message:Binary,
        signature:Binary
    ) -> bool:
        try:
            DSS.new(
                key=ECC.import_key(public_key.get_x(data_format="ascii")),
                mode=MODE,
            ).verify(
                msg_hash=SHA256.new(message.get_x(data_format="bytes")),
                signature=signature.get_x(data_format="bytes"),
            )
            return True
        except ValueError:
            return False