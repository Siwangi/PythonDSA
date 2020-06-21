userInput = int(input("Enter the number: "))
count = 0
prod = 1
while count < userInput:
    prod = prod * (userInput-count)
    count = count + 1
print(prod)
sum = 0
while prod > 0:
    sum = sum + (prod % 10)
    prod = int(prod / 10)
print("sum", sum)