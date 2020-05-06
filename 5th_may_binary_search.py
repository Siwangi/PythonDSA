#search 1 using binary
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def binary(k):
    start = 0
    print("start: ", start)
    end = len(array) -1
    print("end: ", end)
    mid= int((start + end) / 2)
    print("mid: ", mid)
    print("value:", array[mid])
    count = 0
    while start <= end:
        if k == array[mid]:
            count = 1
            print("number found: ", k)
            break

        elif k < array[mid]:
            start = 0
            end = mid - 1
            mid = int((start + end ) / 2)
            print(start, end, mid)

            print("Number less than mid")
        elif k > array[mid]:
            start=mid + 1
            mid = int((start + end) / 2)
            print(start, end, mid)

            print("Number greater than mid")

    if count == 0:
        print("Number not found")


binary(1)