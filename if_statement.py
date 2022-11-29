# if = Do some code IF condition is True
# else = Do something else if above condition/s are False

# ¡X---------------------
#   EXAMPLE 1 IF-ELIF STATEMENT
# ¡X---------------------
age = int(input("Enter your age: "))

if age >= 100:
   print("You are too old to sign up")
elif age >= 20:
   print("You are now signed up")
elif age < 0:
   print("You haven't been born yet")
else:
   print("You must be 20+ sign up")

# ¡X---------------------
#   EXAMPLE 2 ORDER FOOD
# ¡X---------------------
response = input("Do you want food (Y/N)?: ")

if response == "Y" or response == "y":
   print("Have some food")
else:
   print("No food for you!")

# ¡X---------------------
#   EXAMPLE 3 HELLO USER!
# ¡X---------------------
name = input("Enter your name: ")

if name == "":
   print("You did not enter your name!")
else:
   print(f"Hello {name}")

# ¡X---------------------
#   EXAMPLE 4 IF-ELSE STATEMENT
# ¡X---------------------
online = True

if online :
   print("You are online")
else:
   print("You are offline")