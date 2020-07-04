def main():
    userInput = int(input("Enter the count of number: "))
    count = 0
    list = []
    while count < userInput:
        array = int(input("Enter the number: "))
        list.append(array)
        count = count + 1
    print(list)
    for x in range(len(list)):
        for y in range(len(list)-1):
            if list[y] > list[y+1]:
                continue
            elif list[y] < list[y+1]:
                list[y], list[y+1] = list[y+1], list[y]
            print(list)

# def sort(list):
#     for element in range(len(list)):
#         if list[element]


main()


