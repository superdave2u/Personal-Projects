#!/usr/bin/env python3

Name = input("What is your name? ")
Age = input("How old are you? ")
RedditUsername = input("What is your Reddit Username? ")

Output = 'your name is {}, \
you are {} years old, \
and your username is {}'.format(Name, Age, RedditUsername)

print(Output)

with open('outFile', 'w') as f:
    f.write(Output)
