# python3 -m unittest discover -s "./bifas/test" -p "test_*.py"
# python3 -m unittest bifas.test.test_ecdsa.TestECDSA
import unittest

from bifas.utils.data_structure.binary import Binary
from bifas.utils.cryptography.ecdsa import ECDSA

class TestECDSA(unittest.TestCase):
    def test_hard_code_case(self):
        ecdsa_1 = ECDSA(
            passphrase=Binary(
                x="BIFAS",
                data_format="ascii",
            )
        )
        self.assertEqual(b"\x42\x49\x46\x41\x53", ecdsa_1.passphrase.get_x(data_format="bytes"))
        message_1 = Binary(
            x="This is the receipt. Blockchain International Financial Asset System",
            data_format="ascii",
        )
        self.assertEqual(
            ecdsa_1.verify(
                public_key=ecdsa_1.public_key,
                message=message_1,
                signature=ecdsa_1.sign(
                    message=message_1,
                ),
            ),
            True,
        )

        ecdsa_2 = ECDSA(
            passphrase=Binary(
                x="JAAJAT",
                data_format="ascii",
            )
        )
        self.assertEqual(b"\x4a\x41\x41\x4a\x41\x54", ecdsa_2.passphrase.get_x(data_format="bytes"))
        message_2 = Binary(
            x="In the beginning God created the heaven and the earth.",
            data_format="ascii",
        )
        self.assertEqual(
            ecdsa_2.verify(
                public_key=ecdsa_2.public_key,
                message=message_2,
                signature=ecdsa_2.sign(
                    message=message_2,
                ),
            ),
            True,
        )
        self.assertNotEqual(
            ecdsa_1.private_key.get_x(data_format="bytes"),
            ecdsa_2.private_key.get_x(data_format="bytes"),
        )