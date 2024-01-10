empty_list = []
even = [2,4,6,8]
odd = [1,3,5,9]
numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)

# .sort method changes the list in place without creating a new list.
# sorted() function sorts and creates a new list

digits = sorted("432985617")
print(digits) 