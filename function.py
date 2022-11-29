# function = a block of code which is executed only when it is called.

def hello(first_name,last_name,age): # turn the passing value into parameters
    print("hello "+first_name+" "+last_name)
    print("You are "+str(age)+" years old")
    print("Have a nice day!")

hello("USER","NAME",20) # pass arguments to function