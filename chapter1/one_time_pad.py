from secrets import token_bytes
from typing import Tuple


def generate_ramndome_key(length: int = None) -> int:
    token_byte: bytes = token_bytes(nbytes=length)
    return int.from_bytes(token_byte, 'big')


class OneTimePad:
    def __init__(self,  data: str, length: int = None,) -> None:
        self.length: int = length
        self.__key: int = generate_ramndome_key(length=length)
        self.__encrypt_data: int = self.__encrypt(data=data)

    def get_encrypt_data(self) -> int:
        return self.__encrypt_data

    def get_key(self) -> int:
        return self.__key

    def __encrypt(self, data: str) -> int:
        encode_data: bytes = data.encode()
        data_key: int = int.from_bytes(encode_data, 'big')
        return data_key ^ self.__key

    def decrypt(self, data_key: int = None, dummy_key: int = None) -> str:
        if not data_key:
            raise ValueError('key must be valid input')
        if not dummy_key:
            dummy_key = self.__key
        decrypt_data_int: int = dummy_key ^ data_key

        # It was necessary to add 7 to the length of the decrypted data before using integerdivision (//) to divide by 8 to ensure that we “round up,” to avoid an off-by-one error.
        # If our one-time pad encryption truly works, we should be able to encrypt and decrypt
        # the same Unicode string without issue.
        decrypt_data: bytes = decrypt_data_int.to_bytes(
            (decrypt_data_int.bit_length()+7)//8, 'big')
        return decrypt_data.decode()


encrypt = OneTimePad(data='reza')
encrypt_data = encrypt.get_encrypt_data()
print(encrypt.decrypt(data_key=encrypt_data))
