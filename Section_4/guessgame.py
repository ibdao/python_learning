answer = 5
while True: 
    print("Please guess a number between 1 and 10: ")
    guess = int(input())

    if guess == answer:
        print("Good guess!")
        break
    elif guess > answer:
        print("Too high")
    else:
        print("Too low")

