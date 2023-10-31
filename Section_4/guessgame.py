#!/usr/bin/env python3
import random

lowest = random.randint(0, 10)
highest = random.randint(10, 100)
answer = random.randint(lowest, highest)
guess = 0

while guess != answer: 
    print(f"Please guess a number between {lowest} and {highest}: ")
    guess = int(input())
    if guess == 0:
        break

    if guess == answer:
        print("Good guess!")
        break
    elif guess > answer:
        print("Too high")
    else:
        print("Too low")
    
    print("-----")
    print("Press '0' to quit")
