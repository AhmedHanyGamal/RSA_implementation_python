from prime_number_generator import generateLargePrime
from extended_euclidean_algorithm import extended_euclidean_algorithm
from hashlib import sha3_512
from base64 import b64encode, b64decode
import random


class PublicKey:
    def __init__(self, e: int, N: int) -> None:
        self.e = e
        self.N = N

    def encrypt_message(self, message: str) -> int:
        """
        used for privacy and sending messages in a secure way. Can only be decrypted using the corresponding private key.
        """

        ciphertext_base10 = pow(int(message.encode('utf-8').hex(), 16), self.e, self.N)
        ciphertext_bytes = ciphertext_base10.to_bytes((ciphertext_base10.bit_length() + 7) // 8, 'big')
        ciphertext_base64 = b64encode(ciphertext_bytes).decode('utf-8')

        return ciphertext_base64
    

    def authenticate_message(self, message: str, signature):
        """
        used for authentication purposes. Digital signatures and stuff.
        use it authenticate digital signatures and stuff.
        """
        message = message.encode()
        message_digest = sha3_512(message)
        decrypted_signature = pow(signature, self.e, self.N)

        if int(message_digest.hexdigest(), 16) == decrypted_signature:
            return True
        else:
            return False


class PrivateKey:
    def __init__(self, d: int, N: int, phi_N: int) -> None:
        self.d = d
        self.N = N
        self.phi_N = phi_N


    def generate_public_key(self):
        return PublicKey(extended_euclidean_algorithm(self.d, self.phi_N), self.N)
    

    def sign_message(self, message: str):
        """
        used for authentication purposes. Digital signatures and stuff.
        use it for signing stuff.
        """
        message = message.encode()
        message_digest = sha3_512(message)
        return pow(int(message_digest.hexdigest(), 16), self.d, self.N)


    def decrypt_message(self, encrypted_message: str):
        """
        decrypts messages that were encrypted by the corresponding public key.
        used for privacy and sending messages in a secure way. 
        """
        ciphertext_bytes = b64decode(encrypted_message.encode())
        ciphertext_int = int.from_bytes(ciphertext_bytes, 'big')

        return bytes.fromhex(hex(pow(ciphertext_int, self.d, self.N)).lstrip("0x")).decode('utf-8')

def generate_key_pair(prime_number_bits):
    p = generateLargePrime(prime_number_bits)
    q = generateLargePrime(prime_number_bits)
    N = p * q
    phi_N = (p-1) * (q-1)
    e = generateLargePrime(30)
    d = extended_euclidean_algorithm(e, phi_N)
    
    public_key = PublicKey(e, N)
    private_key = PrivateKey(d, N, phi_N)
    return (public_key, private_key)