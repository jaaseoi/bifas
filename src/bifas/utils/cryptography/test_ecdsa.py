# python3 -m unittest bifas.utils.cryptography.test_ecdsa

import unittest

from bifas.utils.data_structure.binary import Binary, init_Binary
from bifas.utils.cryptography.ecdsa import ECDSA

class TestECDSA(unittest.TestCase):
    def test_hard_code_case(self):
        ecdsa = ECDSA(
            passphrase=Binary(
                x="BIFAS",
                data_format="utf-8",
            )
        )
        self.assertEqual(b"\x42\x49\x46\x41\x53", ecdsa.passphrase.get_x(data_format="bytes"))
        message = Binary(
            x="This is the receipt. Blockchain International Financial Asset System",
            data_format="utf-8",
        )
        self.assertEqual(
            ecdsa.verify(
                public_key=ecdsa.public_key,
                message=message,
                signature=ecdsa.sign(
                    message=message,
                ),
            ),
            True,
        )