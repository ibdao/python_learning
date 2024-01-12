data = [104,101,4,105,308,103,5,107,100,306,106,102,108]

min = 100
max = 200

new_data = [x for x in data if min <= x <= max]

print(new_data)