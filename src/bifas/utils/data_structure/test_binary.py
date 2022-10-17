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

if __name__ == "__main__":
    unittest.main()