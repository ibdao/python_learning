# Write a program to print a number of options
# allow the user to select an option from the list

# The options should be numbereed 1 to 9 - although you can you less than 9 options 

start = input("Press Enter to start your day")
options = {1: "Do work",
           2: "Gym",
           3: "Go for a walk",
           0: "Exit"}
decision = ""

while decision != 0:
    decision = int(input("""Please select an activity
        1. Do work
        2. Gym
        3. Go for a walk
        0. Exit 
    """))

    if int(decision) not in options.keys():
        print("Please pick a valid option.")
    else:
        print(f"You chose {options[decision]}")
else:
    print("Goodbye!")

