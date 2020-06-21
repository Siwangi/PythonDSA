
userInput = int(input("Upto how many primes you wanna print: "))

def Prime(userInput):
    count = 1
    sum = 0
    while count <= userInput:
        if userInput % count == 0:
            sum = sum + 1
        count = count + 1

    if sum == 2:
        return "prime"
    else:
        return "not prime"

count = 1
prime = []
sum = 0
while count <= userInput:
    ifPrime = Prime(count)
    if ifPrime == "prime":
        prime.append(count)
        sum = sum + count
    count = count + 1
print(prime, sum)

