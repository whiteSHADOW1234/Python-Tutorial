# *********************************
# if __name__ == '__main__'
# *********************************

# y tho?
# 1. Module can be run as a standalone program
#    or
# 2. Module can be imported and used by other modules

#  Python interpreter sets "special variables", one of which is _name_
#  Python will assign the _name_ variable a value of '__main__' if it's
#  the initial module being run

def main():
    print("running this program directly")


if __name__ == '__main__':
    main()
else:
    print("running this program indirectly")

# *********************************