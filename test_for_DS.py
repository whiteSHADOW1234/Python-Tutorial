array1 = [1,2,3,4,5]

for i in range(len(array1)):
    print(array1[i])
    array1.append(array1[i])

print(array1)