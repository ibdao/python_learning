#!/usr/bin/env python3
available_exits = ["north", "east", "south", "west"]

chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ").lower()
    if chosen_exit == "quit":
        print ("Game over")
        break

print("You escaped!")


# print ([i for i in range(0, 21) if (i % 3 != 0 and i % 5 != 0)])