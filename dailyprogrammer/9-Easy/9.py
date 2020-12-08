#!/usr/bin/env python3

numbers = []
letters = []

while True:
    user_input = input("Input digits or numbers (exit to exit): ")
    if user_input == "exit":
        break
    try:
        val = int(user_input)
        numbers.append(val)
    except ValueError:
        try:
            val = float(user_input)
            numbers.append(val)
        except ValueError:
            letters.append(user_input)


numbers.sort()
letters.sort()

print(numbers)
print(letters)
