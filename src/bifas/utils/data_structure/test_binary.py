# python3 -m unittest bifas.utils.data_structure.test_binary

import unittest

from bifas.utils.data_structure.binary import Binary, int_to_bytes
from bifas.utils.data_structure.date_time import current_date_time_str

NUM_OF_BYTE = 2
NUM_OF_Trials = 10 ** 4

class TestBinary(unittest.TestCase):
    """
    Unit test for bifas.utils.data_structure.binary.Binary for handling binary data from bytes, base64, base16, utf-8, ascii and int.

    See Also
    --------
    bifas.utils.data_structure.binary.Binary
    """

    def test_hard_code_case(self):
        # -------------------------------- bytes --------------------------------
        # bytes -> bytes
        self.assertEqual(Binary(b"\x6b", data_format="bytes").get_x(data_format="bytes"), b"\x6b")   
        self.assertEqual(Binary(b"\x04\x5e", data_format="bytes").get_x(data_format="bytes"), b"\x04\x5e")
        # bytes -> base64
        self.assertEqual(Binary(b"\x6b", data_format="bytes").get_x(data_format="base64"), "aw==")   
        self.assertEqual(Binary(b"\x04\x5e", data_format="bytes").get_x(data_format="base64"), "BF4=")
        # bytes -> base16
        self.assertEqual(Binary(b"\x6b", data_format="bytes").get_x(data_format="base16"), "6b")   
        self.assertEqual(Binary(b"\x04\x5e", data_format="bytes").get_x(data_format="base16"), "45e")
        self.assertEqual(Binary(b"\x61", data_format="bytes").get_x(data_format="base16"), "61")
        # bytes -> int
        self.assertEqual(Binary(b"\x6b", data_format="bytes").get_x(data_format="int"), 107)
        self.assertEqual(Binary(b"\x04\x5e", data_format="bytes").get_x(data_format="int"), 1118)
        # -------------------------------- base64 --------------------------------
        # base64 -> base16
        self.assertEqual(Binary("YQ==", data_format="base64").get_x(data_format="base16"), "61")
        # -------------------------------- base16 --------------------------------
        # base16 -> base16
        self.assertEqual(Binary("61", data_format="base16").get_x(data_format="base16"), "61")
        # -------------------------------- utf-8 --------------------------------
        # utf-8 -> base16
        self.assertEqual(Binary("a", data_format="utf-8").get_x(data_format="base16"), "61")
        # -------------------------------- ascii --------------------------------
        # ascii -> base16
        self.assertEqual(Binary("a", data_format="ascii").get_x(data_format="base16"), "61")
        # -------------------------------- int --------------------------------
        # int -> base16
        self.assertEqual(Binary(97, data_format="int").get_x(data_format="base16"), "61")

    def test_hash_hard_code_case(self):
        question = b"Blockchain International Financial Assets System (BIFAS)"
        answer = "55affbc3b2c2b989f32e3b6cae1ca4bd154a7347adcf380297b484e9d387f5c0"
        self.assertEqual(
            answer,
            Binary(x=question).hash(algo="SHA-256",class_type="Binary").get_x(data_format="base16"),
        )
    
    def test_add_hard_code_case(self):
        a = Binary(x=b"Blockchain International ",data_format="bytes")
        b = Binary(x=b"Financial Assets System (BIFAS)",data_format="bytes")
        self.assertEqual(
            b"Blockchain International Financial Assets System (BIFAS)",
            (a + b).get_x(data_format="bytes"),
        )
    
    def test_iadd_hard_code_case(self):
        a = Binary(x=b"Blockchain International ",data_format="bytes")
        a += Binary(x=b"Financial Assets System (BIFAS)",data_format="bytes")
        self.assertEqual(
            b"Blockchain International Financial Assets System (BIFAS)",
            a.get_x(data_format="bytes"),
        )

if __name__ == "__main__":
    unittest.main()