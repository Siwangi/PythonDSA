userInput = int(input("enter the position of the number: "))

def Prime(userInput):
    count = 1
    sum = 0
    while count <= userInput:
        if userInput % count == 0:
            sum = sum + 1
        count = count + 1
    if sum == 2:
        return "Prime"
    else:
        return "Not prime"
count = 1
sum = 0
while True:
    isPrime = Prime(count)
    if isPrime == "Prime":
        sum = sum + 1
        if sum == userInput:
            print("Prime number would be:", count)
            break
    count = count + 1
