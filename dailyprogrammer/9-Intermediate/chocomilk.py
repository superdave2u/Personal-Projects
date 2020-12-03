#!/usr/bin/env python3

matchString = "I LIEK CHOCOLATE MILK"

with open('random.txt') as f:
    if matchString in f.read():
        print("Match Found")