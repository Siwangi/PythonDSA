def sort_array(array):
    for x in range(len(array)):
        for y in range(len(array) -1 -x):
            if array[y] > array[y+1]:
                array[y], array[y+1] = array[y+1], array[y]
            else:
                continue
    # print(array)
    return array



array = [4,2,7,5,0,12,13]
sort_array(array)



