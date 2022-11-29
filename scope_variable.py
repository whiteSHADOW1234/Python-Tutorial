# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created

name = "Sir" # global scope (available inside & outside functions)

def display_name():
    name = "Move"    # local scope (available only inside this function)
    print(name)

display_name()
print(name)

# LEGB rule:
# L = Local scope
# E = Enclosing function locals
# G = Global scope
# B = Built-in scope
