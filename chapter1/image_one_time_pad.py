import base64
from secrets import token_bytes
from typing import Tuple


def generate_ramndome_key(length: int = None) -> int:
    '''Create randome key for encryption'''
    token_byte: bytes = token_bytes(nbytes=length)
    return int.from_bytes(token_byte, 'big')


def convert_image_to_base64(path: str) -> bytes:
    '''Convert image to base64'''
    with open(file=path, mode='rb') as image_string:
        image_base64: bytes = base64.b64encode(image_string.read())
    return image_base64


def convert_base64_to_image(image_base64: str, image_type: str = 'png') -> None:
    with open('./decrypt_image.'+image_type, 'wb') as image_file:
        image_file.write(base64.b64decode(image_base64))


def encrypt(data: bytes, key: int) -> int:
    print('encrypt start')
    original_key: int = int.from_bytes(data, 'big')
    print('encrypt done')

    return original_key ^ key


def decrypt(key: int, original_key: int) -> str:
    print('decrypt start')
    encrypted_data: int = key ^ original_key
    temp: bytes = encrypted_data.to_bytes(
        (encrypted_data.bit_length()+7)//8, 'big')
    print('decrypt done')
    return temp.decode()


def main():

    image_path: str = input('please enter image path \n')
    image_type = image_path.split('.')[-1]
    key: int = generate_ramndome_key()
    image_base64: bytes = convert_image_to_base64(path=image_path)
    encrypt_data: int = encrypt(data=image_base64, key=key)
    decrypt_data: str = decrypt(key=key, original_key=encrypt_data)
    convert_base64_to_image(image_base64=decrypt_data, image_type=image_type)


if __name__ == '__main__':
    main()
