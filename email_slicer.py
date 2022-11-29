
email = input("Enter your email: ")

username = email[:email.index("@")] # everything before the @
domain = email[email.index("@") + 1:] # everything after the @

print(f"Your username is {username} and domain is {domain}")