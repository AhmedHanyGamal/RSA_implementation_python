from prime_number_generator import generateLargePrime
from extended_euclidean_algorithm import extended_euclidean_algorithm
from hashlib import sha3_512
from base64 import b64encode, b64decode
import random


KEY_BITS = 1024
INPUT_MESSAGE_BLOCK_SIZE = ((KEY_BITS * 2) // 8) - 1
BASE10_BLOCK_SIZE = 616
BASE64_BLOCK_SIZE = 344

# Was trying to figure out an equation to calculate the number of characters in the encrypted message
# no matter the value of KEY_BITS value and the desired base
# didn't work :(
# I was pretty close though (I think)
# BASE10_BLOCK_SIZE = log(pow(2, KEY_BITS * 2), 10)
# BASE64_BLOCK_SIZE = log(pow(2, KEY_BITS * 2), 64)



class PublicKey:
    def __init__(self, e: int, N: int) -> None:
        self.e = e
        self.N = N


    def encrypt_message(self, message: str):
        """
        used for privacy and sending messages in a secure way. Can only be decrypted using the corresponding private key.
        """
        # we need some BLOCKS up in dis bich
        # let's BLOCK dis shit UP
        message_blocks = []
        for i in range(0, len(message), INPUT_MESSAGE_BLOCK_SIZE):
            message_blocks.append(message[i : i + INPUT_MESSAGE_BLOCK_SIZE])

        ciphertext_base64 = ""
        for block in message_blocks:
            encrypted_block = pow(int(block.encode('utf-8').hex(), 16), self.e, self.N)            
            encrypted_block_bytes = encrypted_block.to_bytes((encrypted_block.bit_length() + 7) // 8, 'big')
            ciphertext_base64 += b64encode(encrypted_block_bytes).decode('utf-8')

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
        encrypted_message_blocks = []

        for i in range(0, len(encrypted_message), BASE64_BLOCK_SIZE):
            encrypted_message_blocks.append(encrypted_message[i : i + BASE64_BLOCK_SIZE])


        original_message = ""
        for block in encrypted_message_blocks:
            encrypted_block_bytes = b64decode(block.encode())
            encrypted_block_int = int.from_bytes(encrypted_block_bytes, 'big')
            original_message += bytes.fromhex(hex(pow(encrypted_block_int, self.d, self.N)).lstrip("0x")).decode('utf-8')

        return original_message

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