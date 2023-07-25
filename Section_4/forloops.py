#!/usr/bin/env python3

# parrot = "Norwegian Blue"
# for char in parrot:
#     print(char)

number = "9,223;372:036 854,775;807"
separators = ["" + char for char in number if not char.isnumeric()]

# for char in number:
#     if not char.isnumeric():
#         separators = separators + char
print ("".join(separators))