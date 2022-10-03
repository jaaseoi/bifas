# python3 -m unittest bifas.utils.cryptography.test_hash

import unittest

from bifas.utils.data_structure.binary import Binary
from bifas.utils.cryptography.hash import sha256

class TestBinary(unittest.TestCase):

    def test_hard_code_case(self):
        question = b"Blockchain International Financial Assets System (BIFAS)"
        answer = "55affbc3b2c2b989f32e3b6cae1ca4bd154a7347adcf380297b484e9d387f5c0"
        self.assertEqual(
            answer,
            sha256(Binary(x=question)).get_x(data_type="str"),
        )

if __name__ == "__main__":
    unittest.main()