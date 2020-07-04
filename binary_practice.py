
userInput = int(input("Enter the count in array: "))
count = 0
array = []
while count < userInput:
    userInput1 = int(input("Enter the number: "))
    array.append(userInput1)
    count = count + 1
print("array: ", array)
for x in range(len(array)):
    for y in range(len(array) - 1):
        if array[y] < array[y + 1]:
            continue
        elif array[y] > array[y + 1]:
            array[y], array[y + 1] = array[y + 1], array[y]
        print(array)

userInput2 = int(input("Enter the number to search from the array: "))
mid = int(0 + len(array))/2
print("mid", mid)
if userInput2 == array[int(mid)]:
    print("Got the value:", array[int(mid)])
elif userInput2 < array[int(mid)]:
    start = array[0]
    end = array[int(mid) - 1]
    mid = (start + end )/2
    print("mid1", mid)
    if userInput2 == array[int(mid)]:
        print("Number found in 1", array[int(mid)])


elif userInput2 > array[int(mid)]:
    start = array[int(mid) + 1]
    end = array[len(array)]
    mid2 = (start + end)/2
    print("mid2", mid)
    if userInput2 == array[int(mid2)]:
        print("Number found in 2", array[int(mid2)])


