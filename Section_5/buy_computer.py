current_choice = "-"
computer_parts = []

choices = {
    "1":"computer",
    "2":"monitor",
    "3":"keyboard",
    "4":"mouse",
    "5":"mouse mat",
    "6":"HDMI cable", 
    "7":"dvd drive"
}

while current_choice != '0':
    if len(computer_parts) > 0 and choices[current_choice] in computer_parts:
        print(f"{choices[current_choice]} has already been added")    
    elif current_choice in choices.keys():
        computer_parts.append(choices[current_choice])
        print(f"Adding {choices[current_choice]}...")
        print(f"Your list now contains {computer_parts}.")
    else:
        print("Please add options from the list below: ")
        print(*(f"{choice}: {choices[choice]}\n" for choice in choices))
        print("0: Exit")
    current_choice = input()
print(f"Computer parts: {computer_parts}")
