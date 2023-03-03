import requests
import time
import math

def print_bulk(str, size):
    k = 0
    for c in str:
        if (k % size == 0):
            print(' ', end='')
        print(c, end='')
        k += 1
    print('')



def bruteforce():
    flag = ''
    S_size = math.ceil(26 / 16) * 16 - 1
    characters = "_@}{abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    api = 'https://aes.cryptohack.org/ecb_oracle/encrypt/'

    while True:
        # Generate the expected ciphertext
        S = '1' * (S_size-len(flag))
        url = f'{api}{S.encode().hex()}/'
        expected = requests.get(url).json()['ciphertext']

        print('E: ', end='')
        print_bulk(expected, 32)

        # Bruteforce the character
        for c in characters:
            payload = (S + flag + c).encode().hex()
            url = f'{api}{payload}/'
            res = requests.get(url).json()['ciphertext']

            print(c, ' ', end='')
            print_bulk(res, 32)

            # Compare the second block of the ciphertext
            if res[32:64] == expected[32:64]:
                flag += c
                print(f'flag: {flag}')
                break
            time.sleep(1)

        if flag.endswith('}'):
            break

    print(flag)


bruteforce()

# flag: crypto{p3n6u1n5_h473_3cb}