parrot = "Norwegian Blue"
goal_string = "we win"

print(parrot)

for i in goal_string:
    for j in range(0, len(parrot)):
        if parrot[j] == i:
            print(parrot[j])
            break
    

    

