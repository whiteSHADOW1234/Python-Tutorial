# **kwargs =   parameter that will pack all arguments into a dictionary
#                useful so that a function can accept a varying amount of        
#                  keyword arguments

def hello(**kwargs):
    print(kwargs)
    print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello",end=" ")
    
    # the under code will print the values of the dictionary
    for key,value in kwargs.items():
        print(value,end=" ")
    print()

    # the under code will print the keys of the dictionary
    for value in kwargs.items():
        print(value,end=" ")

    for keys in kwargs.items():
        print(keys,end=" ")


hello(title="Mr.",first="Bro",middle="Dude",last="Code")