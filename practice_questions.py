array = [3, 5, 8, 2, 1]


for x in range(len(array)-1):
    current = array[x+1]
    print("current", current)
    prev = array[x]
    print("prev", prev)
    sum = current + prev
    print("sum",sum)




