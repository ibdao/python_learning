parrot = "Norwegian Blue"
goal_string = "we win"

print(parrot)

# for i in goal_string:
#     for j in range(0, len(parrot)):
#         if parrot[j] == i:
#             print(parrot[j])
#             break
# print()

# for i in goal_string:
#     for j in range(0, len(parrot))[::-1]:
#         if parrot[j] == i:
#             print(parrot[j])
#             break

# print(parrot[0:6]) # Norweg
# print(parrot[3:5]) # we
# print(parrot[0:9]) # Norwegian
# print(parrot[10:]) # Blue

# print(parrot[:6] + parrot[6:] == parrot[:])

letters ="abcedefghijklmnopqrstuvwxyz"

print(parrot[-4:-2]) # Bl
print(parrot[-4:12]) # Bl


print(parrot[0:6:2])
print(parrot[0:6:3])

number = "9,223;372:036 854,775;807"
separators = number[1::4]
values = "".join(char if char not in separators else " " for char in number.split())
print([int(val) for val in values])
