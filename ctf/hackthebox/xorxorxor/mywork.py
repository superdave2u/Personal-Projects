#!/usr/bin/python3
import os

output = '134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9'

lst = []
count = 0
# get every 4'th item
for ITEM in range(0, len(output), 4):
    lst.append(output[ITEM])

# lst.sort()
# unique = list(set(lst))
# lst = unique
print(lst)

# for x in range(0, 256):
#     print(str(x).hex())

for z in range(0, 255):
    for y in range(0, 255):
        # print(z)
        xorvalue = b''
        xorvalue += bytes(hex(z)) ^ bytes(hex(y))
        print(xorvalue)
        # print(xorvalue)
        if xorvalue == any(lst):
            print("maybe match: {}, {}".format(xorvalue, lst))
            if all([xorvalue == x for x in lst]):
                print("wtf: {}".format(xorvalue))

for x in range(0, 254):
    print(hex(x))
 

