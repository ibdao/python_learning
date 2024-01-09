even = [2,4,6,8]
odd = [1,3,5,9]

even.extend(odd)
another_even = even

print(another_even)
even.sort(reverse=True)
print(sorted(even, reverse=True))

