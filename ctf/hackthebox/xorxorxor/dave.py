from tools.idafchev import divide_text_by_blocks,transpose
from tools.idafchev import single_byte_xor,is_printable_text

import itertools

ciphertext  = '134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9'
keysize   = 4
blocks = divide_text_by_blocks(ciphertext, keysize)
print(blocks)
transposed = transpose(blocks)
print(transposed)

all_keys = [] # list of lists. One list for every block. The list has all possible one-byte keys for the block.
for block in transposed:  
    block_keys = [] # store all possible one-byte keys for a single block
    for key in range(256):
        text = single_byte_xor( block , chr(key))
        if is_printable_text(text):
            block_keys.append(chr(key))
    all_keys.append(block_keys)

real_keys = [] # Stores keys with size ks. Generated from all possible combinations of one-byte keys contained in all_keys    
for key in itertools.product(*all_keys):
    real_keys.append( ''.join(key) )

print("Keys to try: {}".format(len(real_keys)))

# # Try every possible multy-byte key.
# for key in real_keys:
#     text = repeating_key_xor(ciphertext,key)
#     if is_english(text):
#         print("Plaintext: {}".format(text))
#         print("Key: {}".format(key))
#         input()
#         print("==================")