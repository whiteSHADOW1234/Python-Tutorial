# type casting = The process of converting a value of one data type to another
#                          (string, integer, float, boolean)
#                          Explicit vs Implicit

name = "Bro"
age = 21
gpa = 1.9
student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(student)) 

age = float(age)
print("Age:",age)

gpa = int(gpa)
print("GPA:",gpa)

student = str(student)
print("Student:",student)

name = bool(name)
print("Name:",name)


print(type(name))
print(type(age))
print(type(gpa))
print(type(student)) 


x = 2
y = 1.0
print(x+y)