#!/usr/bin/#!/usr/bin/env python3
"""
Your challenge for today is to create a random password generator!

For extra credit, allow the user to specify the amount of passwords to
generate.
For even more extra credit, allow the user to specify the length of the strings
he wants to generate!
"""

import string
import secrets


def GenPassword(Length):
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(Length))
    return password


if __name__ == "__main__":
    print(GenPassword(12))
