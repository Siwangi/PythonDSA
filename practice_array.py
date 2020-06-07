userInput = int(input("How many numbers do you want to print in an array: "))
count = 0
array = []
while count < userInput:
    number = int(input("Enter the number: "))
    if number % 5 == 0:
        array.append(number)
    count = count + 1
    print("array: ", array)



