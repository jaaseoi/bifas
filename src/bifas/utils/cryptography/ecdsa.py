# Stateless function of generating private key from arbitrary passphrase, return as utils.data_structure.binary.Binary.
# Stateless function of generating public key from private key, return as utils.data_structure.binary.Binary.
# Stateless function of generating account address from public key, return as utils.data_structure.binary.Binary.
# Stateless function of digital signature from private key and message (utils.data_structure.binary.Binary), return as utils.data_structure.binary.Binary.
# Stateless boolean function to verify digital signed message (utils.data_structure.binary.Binary) with public key (utils.data_structure.binary.Binary).

from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256
from Crypto.Hash import RIPEMD160
from bifas.utils.data_structure.binary import Binary

class ECDSAKeys:

    def __init__(self, passphrase=None) -> None:
        self.private_key_binary, self.public_key_binary = self.generate_key_pairs(passphrase)
        self.address_binary = self.generate_address(self.public_key_binary)
        pass

    def generate_key_pairs(self, passphrase_binary:Binary) -> Binary:

        passphraseIsBinary = type(passphrase_binary) == Binary

        if passphraseIsBinary:
            passphrase = passphrase_binary.get_x(data_format="bytes")
            sha256_hash = SHA256.new(passphrase).hexdigest()
            sha256_hash_int = int(sha256_hash, 16)
            ecc_keys = ECC.construct(curve='P-256', d=sha256_hash_int)
        else:
            ecc_keys = ECC.generate(curve='P-256')

        private_key = ecc_keys.export_key(format='PEM')
        public_key = ecc_keys.public_key().export_key(format='PEM')
        private_key_binary = Binary(x=private_key, data_format='ascii')
        public_key_binary = Binary(x=public_key, data_format='ascii')

        return private_key_binary, public_key_binary

    def generate_address(self, public_key_binary:Binary) -> Binary:
        pass

    def sign(self, private_key_binary:Binary, message_binary:Binary) -> Binary:
        pass

    def verify_signature(self, public_key_binary:Binary, message_binary:Binary) -> bool:
        pass

# Quick test
passphrase = b"For instance, lets say you were planning to build a cheap MAC by concatenating a secret key to a public message m (bad idea!"
keys = ECDSAKeys(passphrase)
print(keys.private_key)
print(keys.public_key)
