import os

source = "test.txt" # this could also be the folder name
destination = "C:\\Users\\Enkai Huang\\Desktop\\destination.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination) 
        # this create a new file (destination) and move the content of source to it (it also delete the source file!!!)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")