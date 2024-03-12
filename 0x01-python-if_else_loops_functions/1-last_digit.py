#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    temp_number *= -1
else:
    temp_number = number
last_digit = temp_number % 10
if number < 0:
    last_digit *= -1
if last_digit > 5:
    print(
            f"Last digit of {number} is "
            f"{last_digit} and is greater than 5"
        )
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
elif last_digit < 6 and last_digit != 0:
    print(
            f"Last digit of {number} is "
            f"{last_digit} and is less than 6and not 0"
            )
else:
    pass
