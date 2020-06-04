userInput = int(input("Enter the number of element that you want to enter in an array: "))
count = 0
new_array = []
while count < userInput:
    array = int(input("Enter the number: "))
    new_array.append(array)
    count = count + 1
print(new_array)
for x in range(len(new_array)):
    for y in range(len(new_array)-1):
        if new_array[y] < new_array[y+1]:
            continue
        elif new_array[y] > new_array[y+1]:
            new_array[y], new_array[y+1] = new_array[y+1], new_array[y]

print("Sorted array: ", new_array)
if new_array[len(new_array)-1] > new_array[len(new_array)-2]:
    print("Second largest number in array:", new_array[len(new_array)-2])

