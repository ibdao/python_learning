#!/usr/bin/env python3

low = 1
high = 1000

print(f"Please think of a number between {low} and {high}")
input("Press ENTER to Start")

guesses = 1

while True:
    print(f" \tGuessing in the range of {low} to {high}.")
    count = low + (high - low) // 2
    high_low = input(
        f"""My guess is {count}. Should I guess higher or lower? \nEnter 'h', 'l' or 'c' if my guess was correct. """).casefold()

    if high_low not in ["h", "l", "c"]:
        print("Please enter 'h', 'l' or 'c'.")
        print()
        
    elif high_low == "c":
        print (f" I got it in {guesses} guesses !")
        break
    
    elif high_low == "h":
        low = count + 1
    else:
        high = count - 1
    
    guesses += 1