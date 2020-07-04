
# userInput = int(input("Enter the count of numbers in array: "))
# count = 0
# prod = 1
# list = []
# while count < userInput:
#     userInput1 = int(input("Enter the number:"))
#     list.append(userInput1)
#     count = count + 1
# print(list)
# for x in list:
#     prod = prod * x
# print(prod)


##optimise

userInput = int(input("Enter the count of numbers in array: "))
count = 0
prod = 1
list = []
while count < userInput:
    userInput1 = int(input("Enter the number:"))
    prod = prod * userInput1
    count = count + 1
    print(prod)