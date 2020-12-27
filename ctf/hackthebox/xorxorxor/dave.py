from tools.idafchev import divide_text_by_blocks,transpose
from tools.idafchev import single_byte_xor,is_printable_text
from tools.idafchev import repeating_key_xor,is_english
from tools.idafchev import has_english_words,has_vowels,has_forbidden_digraphs
from tools.idafchev import has_necessary_percentage_frequent_characters,has_necessary_percentage_punctuation

import itertools
import math
import binascii
from datetime import datetime

cipher_bytes  = binascii.unhexlify('134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9')
keysize   = 4
blocks = divide_text_by_blocks(cipher_bytes, keysize)
print('cipher_bytes',cipher_bytes)
print('blocks',blocks)

transposed_blocks = transpose(blocks)
print('transposed_blocks',transposed_blocks)

all_keys = [] # list of lists. One list for every block. The list has all possible one-byte keys for the block.
for block in transposed_blocks:  
    block_keys = []
    for key in range(256): # brute force
        byte_key=bytes([key])
        try:    
            text = single_byte_xor( block , byte_key).decode('utf-8')
            if is_printable_text(text): # if the input char spits out printable text, save char
                block_keys.append(byte_key)
        except:
            continue

    all_keys.append(block_keys)

real_keys = [] # Stores keys with size ks. Generated from all possible combinations of one-byte keys contained in all_keys    
for key in itertools.product(*all_keys):
    real_keys.append( b''.join(key) )

print('real_key example',real_keys[0])
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
    try:
        text_bytes = repeating_key_xor(cipher_bytes,real_keys[i])
        text=text_bytes.decode('utf-8')

        # if has_english_words( text ):
        #     print("Key: {} - Plaintext: {}".format(real_keys[i],text))
        #     continue

        if not has_vowels( text ):
            continue
    
        if has_forbidden_digraphs( text ):
            continue

        # if not has_necessary_percentage_frequent_characters( text ):
        #     continue

        # if not has_necessary_percentage_punctuation( text ):
        #     continue

        print("Key: {} - Plaintext: {}".format(real_keys[i],text))
    except:
        continue

    progress=progress_floor(i,key_count_to_try)
    output="{} of {} ({}%)".format(i,key_count_to_try,progress)

    if(progress!=last_progress):
        last_progress=progress
        ts_print( output )

ts_print("{} of {} ({}%)".format(key_count_to_try,key_count_to_try,100))