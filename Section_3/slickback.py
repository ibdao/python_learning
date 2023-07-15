letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25::-1]
print(backwards)

# Create a slice that produces the characters qpo
print(letters[16:13:-1])
# Create a slice to produce edcba
print(letters[4::-1])
# Create a slice to produce the last 8 characters in reverse order
print(letters[:17:-1])