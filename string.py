# -------------------------------
# STRING METHODS
# -------------------------------
name = input("Enter your name: ")
phone_number = input("Enter your phone number #: ")

length = len(name)
print("The length of your name is: ", length)
index = name.find(" ")
print("The index of the space is: ", index)
name = name.capitalize()
print("Your name is: ", name)
name = name.upper()
print("Your (upper) name is: ", name)
name = name.lower()
print("Your (lower) name is: ", name)
result = name.isdigit()
print("Is your name a digit? ", result)
result = name.isalpha() # check if all characters are letters
print("Is your name an alpha? ", result)
result = phone_number.count(" ")
print("The number of spaces in your phone number is: ", result)
phone_number = phone_number.replace("-", "")
print("Your phone number is: ", phone_number)

# -------------------------------
#    EXERCISE
# -------------------------------
username = input("Enter a username: ")

if len(username) > 12:
   print("Your name can't be more than 12 characters")
elif not username.find(" ") == -1:
   print("Your username can't contain spaces")
elif not username.isalpha():
   print("Your username can't contain digits")
else:
   print(f"Welcome {username}!")


# -------------------------------
#    HELP METHODS
# -------------------------------
# print(help(str))