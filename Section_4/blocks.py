# for i in range(1, 13):
#     print("No. {0} squared is {1} cubed is {2}".format(i, i**2, i**3))
#     print("*" * 80)
name = input("Please enter your name: ")
age = int(input("How old are you {0}? ".format(name)))

if age >= 18:
    print("You are old enough to vote!")
else:
    print("Please come back in {0} years".format(18 - age))