# python3 -m unittest bifas.utils.data_structure.test_binary

import unittest
import random

from bifas.utils.data_structure.binary import Binary, int_to_bytes
from bifas.utils.data_structure.date_time import current_date_time_str

NUM_OF_BYTE = 2
NUM_OF_Trials = 10 ** 4

class TestBinary(unittest.TestCase):

    def test_hard_code_case(self):
        __tmp_a = {
            "bytes_value": b"\x6b",
            "base64_value": "6b",
            "int_value": 107,
        }
        __tmp_b = {
            "bytes_value": b"\x04\x5e",
            "base64_value": "45e",
            "int_value": 1118,
        }
        __obj_a = Binary(__tmp_a["int_value"])
        __obj_b = Binary(__tmp_b["int_value"])
        
        self.assertEqual(
            b"\x04\x35",
            __obj_a + __obj_b,
        )
        self.assertEqual(Binary(b"\x6b", data_format="bytes") + Binary(b"\x04\x5e"), b"\x04\x35")

        self.assertEqual(Binary(b"\x6b", data_format="bytes").get_x(data_format="bytes"), b"\x6b")   
        self.assertEqual(Binary(b"\x04\x5e", data_format="bytes").get_x(data_format="bytes"), b"\x04\x5e")
        self.assertEqual(Binary(b"\x6b", data_format="bytes").get_x(data_format="base16"), "6b")   
        self.assertEqual(Binary(b"\x04\x5e", data_format="bytes").get_x(data_format="base16"), "45e")
        self.assertEqual(Binary(b"\x6b", data_format="bytes").get_x(data_format="base64"), "aw==")   
        self.assertEqual(Binary(b"\x04\x5e", data_format="bytes").get_x(data_format="base64"), "BF4=")
        self.assertEqual(Binary(b"\x6b", data_format="bytes").get_x(data_format="int"), 107)   
        self.assertEqual(Binary(b"\x04\x5e", data_format="bytes").get_x(data_format="int"), 1118)

        self.assertEqual(Binary(b"\x61", data_format="bytes").get_x(data_format="base16"), "61")
        self.assertEqual(Binary("YQ==", data_format="base64").get_x(data_format="base16"), "61")
        self.assertEqual(Binary("61", data_format="base16").get_x(data_format="base16"), "61")
        self.assertEqual(Binary("a", data_format="utf-8").get_x(data_format="base16"), "61")
        self.assertEqual(Binary("a", data_format="ascii").get_x(data_format="base16"), "61")
        self.assertEqual(Binary(97, data_format="int").get_x(data_format="base16"), "61")

    def __gen_int_str_bytes_test_case(self) -> dict:
        answer = {
            "int_value" : random.randint(
                0,
                2**(NUM_OF_BYTE * 8) - 1,
            ),
        }
        answer["base16_value"] = format(answer["int_value"], "x")
        answer["bytes_value"] = int_to_bytes(answer["int_value"])
        return answer


    def test_init_with_binary(self):
        for i in range(NUM_OF_Trials):
            __tmp = self.__gen_int_str_bytes_test_case()
            print(
                "{} : [INFO] utils.data_structure.test_binary.TestBinary.test_init_with_binary() i={} int_value= {} str_value= {} bytes_value= {}".format(
                    current_date_time_str(),
                    i,
                    __tmp["int_value"],
                    __tmp["base16_value"],
                    __tmp["bytes_value"],
                ),
            )
            __obj = Binary(
                x=__tmp["bytes_value"],
                data_format="bytes",
            )
            self.assertEqual(__obj.get_x(data_format="bytes"), __tmp["bytes_value"])
            self.assertEqual(__obj.get_x(data_format="base16"), __tmp["base16_value"])
            self.assertEqual(__obj.get_x(data_format="int"), __tmp["int_value"])
    
    def test_init_with_base16(self):
        for i in range(NUM_OF_Trials):
            __tmp = self.__gen_int_str_bytes_test_case()
            print(
                "{} : [INFO] utils.data_structure.test_binary.TestBinary.test_init_with_base16() i={} int_value= {} str_value= {} bytes_value= {}".format(
                    current_date_time_str(),
                    i,
                    __tmp["int_value"],
                    __tmp["base16_value"],
                    __tmp["bytes_value"],
                ),
            )
            __obj = Binary(
                x=__tmp["base16_value"],
                data_format="base16",
            )
            self.assertEqual(__obj.get_x(data_format="bytes"), __tmp["bytes_value"])
            self.assertEqual(__obj.get_x(data_format="base16"), __tmp["base16_value"])
            self.assertEqual(__obj.get_x(data_format="int"), __tmp["int_value"])
    
    def test_init_with_int(self):
        for i in range(NUM_OF_Trials):
            __tmp = self.__gen_int_str_bytes_test_case()
            print(
                "{} : [INFO] utils.data_structure.test_binary.TestBinary.test_init_with_int() i={} int_value= {} str_value= {} bytes_value= {}".format(
                    current_date_time_str(),
                    i,
                    __tmp["int_value"],
                    __tmp["base16_value"],
                    __tmp["bytes_value"],
                ),
            )
            __obj = Binary(
                x=__tmp["int_value"],
                data_format="int",
            )
            self.assertEqual(__obj.get_x(data_format="bytes"), __tmp["bytes_value"])
            self.assertEqual(__obj.get_x(data_format="base16"), __tmp["base16_value"])
            self.assertEqual(__obj.get_x(data_format="int"), __tmp["int_value"])
    
    def test_xor(self):
        for i in range(NUM_OF_Trials):
            __tmp_a = self.__gen_int_str_bytes_test_case()
            __tmp_b = self.__gen_int_str_bytes_test_case()
            print(
                "{} : [INFO] utils.data_structure.test_binary.TestBinary.test_xor() i={} int_value= {}, {} str_value= {}, {} bytes_value= {}, {}".format(
                    current_date_time_str(),
                    i,
                    __tmp_a["int_value"],
                    __tmp_b["int_value"],
                    __tmp_a["base16_value"],
                    __tmp_b["base16_value"],
                    __tmp_a["bytes_value"],
                    __tmp_b["bytes_value"],
                ),
            )
            __obj_a = Binary(
                x=__tmp_a["int_value"],
                data_format="int",
            )
            __obj_b = Binary(
                x=__tmp_b["int_value"],
                data_format="int",
            )
            
            self.assertEqual(
                int_to_bytes(__obj_a.get_x(data_format="int") ^ __obj_b.get_x(data_format="int")),
                __obj_a + __obj_b,
            )

if __name__ == "__main__":
    unittest.main()