# def main():
#     computer_parts = [
#         "computer", 
#         "monitor", 
#         "keyboard",
#         "mouse", 
#         "mouse pad"
#         ]

#     for part in computer_parts:
#         print(part)
#     print()
#     print(computer_parts[0:3])

# main()

computer_parts = [
        "computer", 
        "monitor", 
        "keyboard",
        "mouse", 
        "mouse pad"
        ]

print(computer_parts)

# computer_parts[3] = "trackball"
computer_parts[3:] = ["trackball"]
print(computer_parts)