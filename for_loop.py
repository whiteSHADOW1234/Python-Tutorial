# for loops = execute a block of code a fixed number of times.
#                     You can iterate over a range, string, sequence, etc.

# -------------- EXAMPLE 1 (RANGE) --------------

for x in range(1, 11): # stop at the last digit
   print(x)

# -------------- EXAMPLE 2 (REVERSED) --------------

for x in reversed(range(1, 11)):
   print(x)

print("Happy New Year!")

# -------------- EXAMPLE 3 (COUNT BY N) --------------

for x in range(1, 11, 2):
   print(x)

# -------------- EXAMPLE 4 (GET RANGE THROUGH STRING) --------------

credit_card = "1234-5678-9012-3456"

for x in credit_card:
   print(x)

# -------------- EXAMPLE 5 (CONTINUE) --------------

for x in range(1, 21):
   if x == 13:
       continue
   else:
       print(x)

# -------------- EXAMPLE 6 (BREAK) --------------

for x in range(1, 21):
   if x == 13:
       break
   else:
       print(x)