# collection = single "variable" that can hold multiple values
# including Lists, Tuples and Sets


#   List  = [] ordered and changeable. Duplicates OK
# fruits = ["apple", "banana", "cherry", "apple", "cherry"]
# # print(dir(fruits))
# # print(help(fruits))
# print(fruits.index("banana"))
# print(fruits.count("apple"))
# for fruit in fruits:
#     print(fruit)
# print(fruits[0])
# print(fruits)
# fruits[1] = "blackcurrant"
# print(fruits)
# print(len(fruits))
# fruits.append("orange")
# print(fruits)
# fruits.insert(1, "grape")
# print(fruits)
# fruits.remove("apple") # only remove the first one
# print(fruits)
# fruits.reverse()
# print(fruits)
# fruits.sort()
# print(fruits)
# fruits.pop()
# print(fruits)
# del fruits[0]
# print(fruits)
# fruits.clear()
# print(fruits)


#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
# zoo = {"zebra", "lion", "tiger", "elephant", "lion"}
# # print(dir(zoo))
# # print(help(zoo))
# # print(len(zoo))
# print("apple" in zoo)
# print(zoo)
# zoo.add("giraffe")
# print(zoo)
# zoo.remove("lion")
# print(zoo)
# zoo.pop() # remove random item
# print(zoo)
# zoo.discard("tiger") # remove item if it exists
# print(zoo)
# zoo.clear()
# print(zoo)


#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER
colors = ("red", "green", "blue", "red", "blue")
# print(dir(colors))
# print(help(colors))
print(colors[0])
print(colors)
# colors[1] = "black" # error
# print(colors)
print(len(colors))
print(colors.count("red"))
print(colors.index("blue"))
for color in colors:
    print(color)