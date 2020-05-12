# add 5 to all the elements in the array using append and without append
array = [1, 4, 2, 6]

for element in array:
    element = element + 5
    print("new array: ", element)

new_array1 = []
for element in array:
    element = element + 5
    new_array1.append(element)
    print("new array1: ", new_array1)

for element in array:
    element = element + 5
    print("array:", array)


for element in range(len(array)):
    array[element] = array[element] + 5
    print("arr:", array)

new_array2 = []
for element in range(len(array)):
    element = array[element] + 5
    new_array2.append(element)
    print("new array2:", new_array2)

