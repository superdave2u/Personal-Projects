#!/usr/bin/env python3

import codecs


def encode(s):
    return codecs.encode(s, "rot13")


def decode(s):
    return codecs.decode(s, "rot13")


if __name__ == "__main__":
    print(decode(encode("Hi Mom")))
