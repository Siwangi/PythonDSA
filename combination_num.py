#print combination of two number:

array=[2, 6, 3, 4, 1]
count=0
for x in range(len(array)):
    print("value of x: ", array[x])
    for y in range(x+1, len(array)):
        print("value of xy: ", array[x], array[y])
        sum = array[x]+ array[y]
        print("sum:", sum)
        if array[x] + array[y] == 5:
            count = count + 1
            print("Number of count: ", count, "pair:", array[x], array[y] )
        else:
            print("Number do not exists")
print("count:", count)
