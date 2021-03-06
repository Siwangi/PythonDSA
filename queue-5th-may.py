def GetChoice():
    print()
    print(" P == Print the array ")
    print(" PU == Push in the array")
    print(" PO == Pop in the array")
    print(" Q == Quit")
    print()
    UserChoice=input("Enter choice:  ")
    print()
    UserChoice=UserChoice.upper()
    return UserChoice

array=[1, 2, 3, 4, 5, 6]


def Print():
    print("array: ", array)


def Push():
    print("Enter number to push")
    try:
        userinput=int(input("number: "))
        array.append(userinput)
        print("New array: ", array)
    except ValueError:
        print("Error Message: You can only push number in this array")


def Pop():
    count=0
    print("Enter number to pop")
    try:
        userinput=int(input("number: "))
        for i in array:
            if userinput == i:
                count = 1
        if count == 0:
            print("Error Message: Number entered is not in array")

        elif userinput != array[0]:
            print("Error Message: You only pop first element in a Queue")
        elif userinput == array[0]:
            array.remove(userinput)
            print("New array: ", array)

        elif len(array) == 0:
            print("Error Message: Array is empty")

    except ValueError:
        print("Error Message: You can only pop number in this array")


def main():
    while True:
        Choice=GetChoice()
        if Choice == 'P':
            Print()
        elif Choice == 'PU':
            Push()
        elif Choice == 'PO':
            Pop()
        elif Choice == "Q":
            exit()
        else:
            print("Please enter options only")


main()





