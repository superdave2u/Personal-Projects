from tools.cipher import get_key_length, get_key, decrypt

ciphertext='134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9'

key_length=4
print("Key length is most likely {}".format(key_length))

key = get_key(ciphertext, key_length)
plaintext = decrypt(ciphertext, key)

print("Key: {}".format(key))
print("Plaintext: {}".format(plaintext))