array = [3, 1, 9, 4, 8, 5, 12, 2]




for x in range(len(array)):
    for y in range(len(array)-1):
        if array[y] < array[y + 1]:
            continue

        elif array[y] > array[y+1]:
            array[y], array[y+1] = array[y+1], array[y]
    print(array)


print(array)





