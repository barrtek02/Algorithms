from task3 import egcd
from task4 import power_modulo, is_prime_miller_rabin
import random

def generate_prime_number(bit_length=10):
    while True:
        num = random.getrandbits(bit_length)
        if is_prime_miller_rabin(num):
            return num

def generate_rsa_keypair(p, q):
    """ Function for generating an RSA key pair."""
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 0
    while True:
        e = random.randint(2, phi - 1)
        if egcd(e, phi) == 1:
            break

    d = pow(e, -1, phi)

    return (e, n), (d, n)

def encrypt_number(number, public_key):
    e, n = public_key
    return power_modulo(number, e, n)

def decrypt_number(encrypted_number, private_key):
    d, n = private_key
    return power_modulo(encrypted_number, d, n)

def encrypt_str(string, public_key, p, q):

    private_message = []
    integer = 1
    for char in string:
        integer = integer * 256 + ord(char)
        if integer > p * q:
            private_message.append((integer-ord(char))//256)
            integer = ord(char)
    if integer > 1:
        private_message.append(integer)

    private_message = [str(encrypt_number(number, public_key)) for number in private_message]
    return ','.join(private_message)


def decrypt_str(private_message, private_key):
    private_message = [decrypt_number(int(number), private_key) for number in private_message.split(',')]
    message = []
    for number in private_message[::-1]:
        while number > 0:
            char = chr(number % 256)
            message.append(char)
            number = number // 256
    return ''.join(message[0:-1][::-1])


if __name__ == '__main__':

    # p = 9323
    # q = 7879
    bit_length = 7
    # bit_length = 40
    p, q = generate_prime_number(bit_length), generate_prime_number(bit_length)

    message = 'abcdefghi'
    public_key, private_key  = generate_rsa_keypair(p, q)
    private_message = encrypt_str(message, public_key, p, q)
    decrypted_message = decrypt_str(private_message, private_key)
    print(f'message: {message}\n'
          f'private_message: {private_message}\n'
          f'decrypted_message: {decrypted_message}\n')

    message = 'Hello word'
    # public_key, private_key  = generate_rsa_keypair(p, q)
    private_message = encrypt_str(message, public_key, p, q)
    decrypted_message = decrypt_str(private_message, private_key)
    print(f'message: {message}\n'
          f'private_message: {private_message}\n'
          f'decrypted_message: {decrypted_message}\n')


