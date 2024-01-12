data = [4,5,104,105,110,120,130,130,150,160,170,183,183,187,188,191,350,360]

min = 100
max = 200

new_data = [x for x in data if min <= x <= max]

print(new_data)
