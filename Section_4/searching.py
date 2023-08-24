#!/usr/bin/env python3

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "spam"

if item_to_find in shopping_list:
    print(f"{item_to_find} found at position {shopping_list.index(item_to_find)}")
else:
    print(f"{item_to_find} not in list")
