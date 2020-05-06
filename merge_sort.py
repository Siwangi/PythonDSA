#merge sort :
array = [3, 9, 1, 7, 2, 6]
start = 0
end = len(array)
mid = int((start+end) / 2)
print("mid index: ", mid)
print("mid index value: ", array[mid])
# print(len(array))
# print(array[len(array) - 1])
# print(len(array) - 1)
for x in range(start, mid):
    for y in range(mid + 1, len(array)):
        start = 0
        end = mid
        mid = int((start + end) / 2)
        print("new mid index for the first half: ", mid)
        print("new mid index value for the first half: ", array[mid])
        if array[start] < array[mid]:
            continue
        elif array[start] > array[mid]:
            array[start], array[mid] = array[mid], array[start]
            print("After swap array1: ", array[start], array[mid])
            start = mid + 1
            # end = len(array)
            mid = int((start+end)/2)
        elif array[start] < array[mid]:
            array[start], array[mid]=array[mid], array[start]
            print("After swap array2: ", array)
        elif array[start] < array[mid]:
            continue
print("final: ", array)
