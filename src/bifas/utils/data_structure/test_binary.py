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
            "str_value": "6b",
            "int_value": 107,
        }
        __tmp_b = {
            "bytes_value": b"\x04\x5e",
            "str_value": "45e",
            "int_value": 1118,
        }
        __obj_a = Binary(__tmp_a["int_value"])
        __obj_b = Binary(__tmp_b["int_value"])
        
        self.assertEqual(
            b"\x04\x35",
            __obj_a + __obj_b,
        )
        self.assertEqual(Binary(b"\x6b") + Binary(b"\x04\x5e"), b"\x04\x35")

        self.assertEqual(Binary(b"\x6b").get_x(data_type="bytes"), b"\x6b")   
        self.assertEqual(Binary(b"\x04\x5e").get_x(data_type="bytes"), b"\x04\x5e")
        self.assertEqual(Binary(b"\x6b").get_x(data_type="str"), "6b")   
        self.assertEqual(Binary(b"\x04\x5e").get_x(data_type="str"), "45e")
        self.assertEqual(Binary(b"\x6b").get_x(data_type="int"), 107)   
        self.assertEqual(Binary(b"\x04\x5e").get_x(data_type="int"), 1118)

    def __gen_int_str_bytes_test_case(self) -> dict:
        answer = {
            "int_value" : random.randint(
                0,
                2**(NUM_OF_BYTE * 8) - 1,
            ),
        }
        answer["str_value"] = format(answer["int_value"], "x")
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
                    __tmp["str_value"],
                    __tmp["bytes_value"],
                ),
            )
            __obj = Binary(__tmp["bytes_value"])
            self.assertEqual(__obj.get_x(data_type="bytes"), __tmp["bytes_value"])
            self.assertEqual(__obj.get_x(data_type="str"), __tmp["str_value"])
            self.assertEqual(__obj.get_x(data_type="int"), __tmp["int_value"])
    
    def test_init_with_str(self):
        for i in range(NUM_OF_Trials):
            __tmp = self.__gen_int_str_bytes_test_case()
            print(
                "{} : [INFO] utils.data_structure.test_binary.TestBinary.test_init_with_str() i={} int_value= {} str_value= {} bytes_value= {}".format(
                    current_date_time_str(),
                    i,
                    __tmp["int_value"],
                    __tmp["str_value"],
                    __tmp["bytes_value"],
                ),
            )
            __obj = Binary(__tmp["str_value"])
            self.assertEqual(__obj.get_x(data_type="bytes"), __tmp["bytes_value"])
            self.assertEqual(__obj.get_x(data_type="str"), __tmp["str_value"])
            self.assertEqual(__obj.get_x(data_type="int"), __tmp["int_value"])
    
    def test_init_with_int(self):
        for i in range(NUM_OF_Trials):
            __tmp = self.__gen_int_str_bytes_test_case()
            print(
                "{} : [INFO] utils.data_structure.test_binary.TestBinary.test_init_with_int() i={} int_value= {} str_value= {} bytes_value= {}".format(
                    current_date_time_str(),
                    i,
                    __tmp["int_value"],
                    __tmp["str_value"],
                    __tmp["bytes_value"],
                ),
            )
            __obj = Binary(__tmp["int_value"])
            self.assertEqual(__obj.get_x(data_type="bytes"), __tmp["bytes_value"])
            self.assertEqual(__obj.get_x(data_type="str"), __tmp["str_value"])
            self.assertEqual(__obj.get_x(data_type="int"), __tmp["int_value"])
    
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
                    __tmp_a["str_value"],
                    __tmp_b["str_value"],
                    __tmp_a["bytes_value"],
                    __tmp_b["bytes_value"],
                ),
            )
            __obj_a = Binary(__tmp_a["int_value"])
            __obj_b = Binary(__tmp_b["int_value"])
            
            self.assertEqual(
                int_to_bytes(__obj_a.get_x(data_type="int") ^ __obj_b.get_x(data_type="int")),
                __obj_a + __obj_b,
            )

if __name__ == "__main__":
    unittest.main()