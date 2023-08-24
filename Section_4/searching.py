#!/usr/bin/env python3

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "spam"

for index, item in enumerate(shopping_list):
    if item is item_to_find:
        print(f"Buy {item} at {index}")
        break
