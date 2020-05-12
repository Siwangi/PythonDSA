array = [6, 9, 2, 4, 5, 1]
print("length of array : ", len(array))
def mergeSort(array):
    print("Splitting ",array)
    if len(array)>1:
        mid = len(array)//2
        lefthalf = array[:mid]
        righthalf = array[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0
        print("length of lefthalf : ", len(lefthalf))
        print("length of righthalf : ", len(righthalf))
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                array[k]=lefthalf[i]
                i=i+1
            else:
                array[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            array[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            array[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",array)

array = [6, 9, 2, 4, 5, 1]
mergeSort(array)
print(array)

