import os 

from tools.idafchev import single_byte_xor,break_single_byte_xor

msg = 'This is a very secret message!'
print("Plaintext",msg)

key = os.urandom(1)

print("Key as hex",key.hex())
print("Key as encode",key)

ciphertext = single_byte_xor(msg.encode(), key)

print('Ciphertext (hex)', ciphertext.hex())

keys, plaintext = break_single_byte_xor(ciphertext)
for i in range(len(keys)):
    print(keys[i], plaintext[i])