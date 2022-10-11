# python3 -m unittest bifas.utils.cryptography.test_rsa

import unittest
import random
import string

from bifas.utils.data_structure.binary import Binary, init_Binary
from bifas.utils.cryptography.rsa import RSA

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

class TestRSA(unittest.TestCase):
    
    def test_gcd(self):
        for _ in range(16):
            rsa = RSA(
                n_bits=4096,
            )
            payload = init_Binary(get_random_string(16))
            cipher = rsa.public_key.encrypt(
                message=init_Binary(payload),
            )
            self.assertEqual(
                rsa.private_key.decrypt(
                    message=init_Binary(cipher),
                ).get_x(data_format="bytes"),
                payload.get_x(data_format="bytes"),
            )
if __name__ == "__main__":
    unittest.main()