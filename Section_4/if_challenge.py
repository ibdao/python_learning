#!/usr/bin/env python3
name = input("Who are you? ")
age = int(input("Hello {}, how old are you? ".format(name)))

if name and 18 <= age <= 30: 
    print("Welcome to the holiday")
else:
    print("GTFO")