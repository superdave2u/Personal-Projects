from tools.idafchev import divide_text_by_blocks,transpose
from tools.idafchev import single_byte_xor,is_printable_text
from tools.idafchev import repeating_key_xor,is_english

import itertools
import math
from datetime import datetime

ciphertext  = '134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9'
keysize   = 4
blocks = divide_text_by_blocks(ciphertext, keysize)
print(blocks)
transposed = transpose(blocks)
print(transposed)

all_keys = [] # list of lists. One list for every block. The list has all possible one-byte keys for the block.
for block in transposed:  
    block_keys = []
    for key in range(128): # brute force
        text = single_byte_xor( block , chr(key))
        if is_printable_text(text): # if the input char spits out printable text, save char
            block_keys.append(chr(key))
    all_keys.append(block_keys)

real_keys = [] # Stores keys with size ks. Generated from all possible combinations of one-byte keys contained in all_keys    
for key in itertools.product(*all_keys):
    real_keys.append( ''.join(key) )

key_count_to_try=len(real_keys)
print("Keys to try: {}".format(key_count_to_try))

def progress_floor(i , key_count_to_try):
    progress= i / key_count_to_try * 100
    return math.floor(progress)

def ts_print(content):
    timestamp = datetime.now().isoformat()
    print("{}: {}".format(timestamp,content))
    pass

last_progress=0
ts_print("{} of {} ({}%)".format(0,key_count_to_try,0))

for i in range(key_count_to_try):
    text = repeating_key_xor(ciphertext,real_keys[i])
    if is_english(text):
        print("Plaintext: {}".format(text))
        print("Key: {}".format(real_keys[i]))
        input()
        print("==================")
        
    progress=progress_floor(i,key_count_to_try)
    output="{} of {} ({}%)".format(i,key_count_to_try,progress)
    
    if(progress!=last_progress):
        last_progress=progress
        ts_print( output )

ts_print("{} of {} ({}%)".format(key_count_to_try,key_count_to_try,100))