# indexing = accessing elements of a sequence using [] (indexing operator)
#                     [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0]) # prints the starting index
print(credit_number[0:4]) # prints the starting index but not the ending index
print(credit_number[:4]) # starting index is initially 0
print(credit_number[4:8])
print(credit_number[4:]) # the ending index is initially the last index +1
print(credit_number[-1]) # prints the last index
print(credit_number[-4:]) # prints the last 4 indexes
print(credit_number[::2]) # counts by 2
print(credit_number[::3]) # counts by 3

# ---------------------------------------
# EXERCISE 1
# ---------------------------------------
credit_number = "1234-5678-9012-3456"
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

# ---------------------------------------
# EXERCISE 2
# ---------------------------------------
credit_number = "1234-5678-9012-3456"
credit_number = credit_number[::-1] # reverses the string
print(credit_number)