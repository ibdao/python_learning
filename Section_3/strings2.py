parrot = "Norwegian Blue"
goal_string = "we win"

print(parrot)

for i in goal_string:
    for j in range(0, len(parrot) - 1):
        if parrot[j] == i:
            print(parrot[j])
    

    

