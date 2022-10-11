from Crypto.PublicKey import RSA as pycryptodome_RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

from bifas.utils.data_structure.binary import Binary, init_Binary

class PublicKey():
    def __init__(
        self,
        key:Binary,
    ) -> None:
        self.key = key

    def encrypt(
        self,
        message:Binary,
    ) -> Binary:
        data = message.get_x(data_format="bytes")
        key = pycryptodome_RSA.import_key(self.key.get_x(data_format="bytes"))
        sessionKey = get_random_bytes(16)
        cipherRSA = PKCS1_OAEP.new(key)
        encSessionKey = cipherRSA.encrypt(sessionKey)
        cipherAES = AES.new(sessionKey, AES.MODE_EAX)
        ciphertext, tag = cipherAES.encrypt_and_digest(data)
        return init_Binary(
            x= encSessionKey + cipherAES.nonce + tag  + ciphertext,
        )

class PrivateKey():
    def __init__(
        self,
        key:Binary,
    ) -> None:
        self.key = key

    def decrypt(
        self,
        message:Binary,
    ) -> Binary:
        privateKey = pycryptodome_RSA.import_key(self.key.get_x(data_format="bytes"))
        pointer = privateKey.size_in_bytes()
        __tmp_message = message.get_x(data_format="bytes")
        encSessionKey = __tmp_message[:pointer]
        nonce = __tmp_message[pointer:pointer+16]
        pointer += 16
        tag = __tmp_message[pointer:pointer+16]
        ciphertext = __tmp_message[pointer+16:]
        cipherRSA = PKCS1_OAEP.new(privateKey)
        sessionKey = cipherRSA.decrypt(encSessionKey)
        cipherAES = AES.new(sessionKey, AES.MODE_EAX, nonce)
        data = cipherAES.decrypt_and_verify(ciphertext, tag)
        return init_Binary(x=data)

class RSA():
    def __init__(
        self,
        public_key:PublicKey=None,
        private_key:PrivateKey=None,
        n_bits:int=4096,
    ) -> None:
        if not((type(public_key) == PublicKey) and (type(private_key) == PrivateKey)):
            key = pycryptodome_RSA.generate(n_bits)
            self.private_key= PrivateKey(init_Binary(key.export_key()))
            self.public_key = PublicKey(init_Binary(key.publickey().export_key()))
        else:
            self.private_key= private_key
            self.public_key = public_key