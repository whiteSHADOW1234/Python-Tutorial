# dictionary =  a collection of {key:value}(= item) pairs
#                        ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
print(capitals.get("Japan"))

if capitals.get("Russia"):
   print("That capital exists")
else:
   print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"})
print(capitals)
capitals.update({"USA": "Detroit"})
print(capitals)
capitals.pop("China")
print(capitals)
capitals.popitem()
print(capitals)
# capitals.clear()
# print(capitals)

keys = capitals.keys()
print(keys)
for key in capitals.keys():
  print(key)

values = capitals.values()
print(values)
for value in capitals.values():
    print(value)

items = capitals.items()
print(items)
for key, value in capitals.items():
   print(f"{key}: {value}")