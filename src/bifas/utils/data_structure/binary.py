import typing
import math
import base64

from bifas.utils.data_structure.date_time import current_date_time_str

def int_to_bytes(
    x:int = 0,
    endianness:typing.Literal["big","little"]="big",
    signed_flag=False,
) -> bytes:
    if (x == 0):
        return b"\x00"
    return x.to_bytes(
        length=math.ceil(
            math.log(
                x + 1,  # prevent  boundary case of 256, 65536, ...
                2 ** 8,
            ),
        ),
        byteorder=endianness,
        signed=signed_flag,
    )

class Binary():
    """
    Generic class for handling binary data.

    See Also
    --------
    bifas.utils.cryptography.hash.sha256
    """
    def __init__(
        self,
        x:typing.Union[
            bytes,
            str,
            int,
        ]=None,
        data_format:typing.Literal[
            "bytes",
            "base64",
            "utf-8",
            "ascii",
            "int",
        ]="base64",
        endianness:typing.Literal["big","little"]="big",
        signed_flag=False,
    ) -> None:
        self.__x = None
        if (x != None):
            self.endianness = endianness
            self.signed_flag = signed_flag
            if (type(x) == bytes):
                self.__x = x
            elif (type(x) == str):
                if (data_format == "base64"):
                    self.__x = base64.b64decode(x)
                elif (data_format == "base16"):
                    x = int(x, 16)
                    self.__x = int_to_bytes(x)
                elif (data_format == "utf-8"):
                    self.__x = bytes(x, "utf-8")
                elif (data_format == "ascii"):
                    self.__x = bytes(x, "ascii")
            elif (type(x) == int):
                self.__x = int_to_bytes(x)
            else:
                raise Exception(
                    "{} : [CRITICAL] bifas.utils.data_structure.binary.Binary.__init__() unknown type of x = {}".format(
                        current_date_time_str(),
                        x,
                    )
                )

    def get_x(
        self,
        data_format:typing.Literal[
            "bytes",
            "base64",
            "base16",
            "int",
        ]="bytes"
    ) -> typing.Union[
        bytes,
        str,
        int,
    ]:
        """
        Generic function to return the value in various format.

        Parameters
        ----------
        data_format : typing.Literal[
            "bytes",
            "base64",
            "base16",
            "int",
        ], default "bytes"

        Returns
        -------
        typing.Union[
            bytes,
            str,
            int,
        ]
            The value with respective data type.

        Examples
        --------
        >>> from utils.data_structure.binary import Binary
        >>> Binary(b"\x6b").get_x(data_format="bytes") == b"\x6b"
        True
        >>> Binary(b"\x04\x5e").get_x(data_format="bytes") == b"\x04\x5e"
        True
        >>> Binary(b"\x6b").get_x(data_format="base64") == "6b"
        True
        >>> Binary(b"\x04\x5e").get_x(data_format="base64") == "45e"
        True
        >>> Binary(b"\x6b").get_x(data_format="int") == 107
        True
        >>> Binary(b"\x04\x5e").get_x(data_format="int") == 1118
        True
        """
        if (self.__x == None):
            return None
        else:
            if (data_format == "bytes"):
                return self.__x
            elif (data_format == "base64"):
                return base64.b64encode(self.__x).decode('ascii')
            elif (data_format == "base16"):
                return format(int.from_bytes(bytes=self.__x,byteorder=self.endianness, signed=self.signed_flag), "x")
            
            elif (data_format == "int"):
                return int.from_bytes(bytes=self.__x,byteorder=self.endianness, signed=self.signed_flag)
            else:
                raise Exception(
                    "{} : [CRITICAL] bifas.utils.data_structure.binary.Binary.get_x() unknown data_format = {}".format(
                        current_date_time_str(),
                        data_format,
                    )
                )
    
    def __add__(self, x2) -> bytes:
        """
        XOR logical operation on two binary number.

        This function simply wraps the ``+`` operator to perform XOR logical operation on two Binary class objects.

        Parameters
        ----------
        self :
            Operand A.
        x2 : Binary
            Operand B.

        Returns
        -------
        bytes
            The XOR of ``self`` and ``x2``.

        See Also
        --------

        Examples
        --------
        >>> from utils.data_structure.binary import Binary
        >>> Binary(b"\x6b") + Binary(b"\x04\x5e") == b"\x04\x35"
        True
        """
        if ((self.__x == None) or (x2.get_x(data_format="int") == None)):
            return None
        else:
            return int_to_bytes(self.get_x(data_format="int") ^ x2.get_x(data_format="int"))

def init_Binary(
    x:typing.Union[
        Binary,
        bytes,
        str,
        int,
    ]=None,
    **kwargs,
) -> Binary:
    if (type(x) == Binary):
        return x
    else:
        return Binary(
            x=x,
            **kwargs,
        )