# -------------------------------------------------------------------
# sort() method   = used with lists
# sort() function = used with iterables

# students = ["Squidward", "Spongebob", "Patrick", "Mr. Krabs", "Sandy"]
# students.sort()
# print(students)
# for i in students:
#     print(i)

# students.sort(reverse=True)
# print(students)
# for i in students:
#     print(i)

# -------------------------------------------------------------------
# students = ("Squidward", "Spongebob", "Patrick", "Mr. Krabs", "Sandy")
# sortedstudents = sorted(students,reverse=True)
# print(sortedstudents)
# for i in sortedstudents:
#     print(i)

# -------------------------------------------------------------------

students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick","D", 36),
            ("Spongebob","B", 20),
            ("Mr.Krabs","C", 78))

grade = lambda grades:grades[1]
sorted_students = sorted(students,key=grade) # sorts and creates a new list

for i in sorted_students:
    print(i)
# -------------------------------------------------------------------

# students = [("Squidward", "F", 60),
#             ("Sandy", "A", 33),
#             ("Patrick","D", 36),
#             ("Spongebob","B", 20),
#             ("Mr.Krabs","C", 78)]

# age = lambda ages:ages[2]
# students.sort(key=age)                     # sorts current list

# for i in students:
#     print(i)