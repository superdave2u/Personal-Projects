#!/usr/bin/env python3

import getpass

Username = input("Enter your username? ")
Password = getpass.getpass(prompt='Password: ', stream=None)

with open('username.txt', 'r') as f:
    FileUsername = f.readlines()

with open('password.txt', 'r') as f:
    FilePassword = f.readline()

if Username is FileUsername and Password is FilePassword:
    print("Login Successful")
else:
    print("Login Failed")
