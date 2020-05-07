array = [1, 2, 3, 4, 5]
for x in array:
    print("array value:", x)
for x in range(len(array)):
    print("range index:", x)
    print("range value: ", array[x])
for x in range(len(array)- 1):
    print("range in len minus one:", x)
    print("range value in len minus one::", array[x])

for x in array:
    print("array value for key(x) & value(a1)(starts from 0 so a1 is index ):", array[x])