#!/usr/bin/python3
import os
# flag = open('flag.txt', 'r').read().strip().encode()
flag = '13111111111'.encode()


class XOR:
    def __init__(self):
        # Generate random bytes, 4 length. 
        # returned in byte format, hexademical.
        self.key = os.urandom(4)
        print(self.key)
    def encrypt(self, data: bytes) -> bytes:

        # Define a new variable, in string format.
        xored = b''

        # for i in start: 0, end: len data, step: 1
        for i in range(len(data)):
            # print(data[i])
            print(i % len(self.key))
            # xored variable is string, that recieves "additions" as the loop progresses
            xored += bytes([data[i] ^ self.key[i % len(self.key)]])
            # print(bytes([data[i] ^ self.key[i % len(self.key)]]))
            #                                   i = range, i%key will be, 0,1,2,3
        return xored
    def decrypt(self, data: bytes) -> bytes:
        return self.encrypt(data)

def main():
    global flag
    crypto = XOR()
    print ('Flag:', crypto.encrypt(flag).hex())

if __name__ == '__main__':
    main()
