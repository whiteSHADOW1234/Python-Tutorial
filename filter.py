# filter() =    creates a collection of elements from an iterable,
#               for which a function returns true
#
#               filter(function, iterable)

friends = [("Spongebob", 20),( "Patrick", 36),("Sandy", 33),("Mr.Krabs", 78),("Squidward", 60)]
age = lambda data:data[1] >= 30
over_30 = list(filter(age, friends))
print(over_30)
for i in over_30:
    print(i)