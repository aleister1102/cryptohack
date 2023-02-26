from pwn import *

# flag: crypto{0x10_15_my_f4v0ur173_by7e}
enc = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

for i in range(0,256):
    byte = int.to_bytes(i)
    print(xor(enc, byte))

# flag: crypto{x0r_i5_ass0c1at1v3}
key1 = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
key2_key1 = bytes.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e')
key2_key3 = bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
enc = bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')

key2 = xor(key1, key2_key1)
key3 = xor(key2, key2_key3)
flag = xor(enc, key3, key2, key1)
print(flag)

# flag: crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}
enc = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
key = b'myXORkey'

print(xor(enc, key))

