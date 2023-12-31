#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = number % 10 if number >= 0 else number % -10
out_text_last = f"Last digit of {number} is "

if last_digit > 5:
    print(f"{out_text_last}{last_digit:d} and is greater than 5")
elif last_digit < 6 and last_digit != 0:
    print(f"{out_text_last}{last_digit:d} and is less than 6 and not 0")
else:
    print(f"{out_text_last}{last_digit:d} and is 0")
