def calculator():
    print("ME == Show the Menu")
    print("A == Addition")
    print("S == Subtraction")
    print("D == Division")
    print("MU == Multiplication")
    print("Q == Quit")

    userChoice = input("Enter your Choice: ")
    userChoice = userChoice.upper()
    return userChoice


def Menu():
    print("Menu")



def Addition():
    print("Enter the numbers below to Add")
    try:
        userInput = int(input("how many numbers do you want to add: "))
        count = 0
        sum = 0
        while count < userInput:
            userInput1 = int(input("Enter the number: "))
            sum = sum + userInput1
            count = count +1
        print("Addition: ", sum)
    except ValueError:
        print("Error Message: You can only enter Numbers")


def Subtraction():
    print("Enter the numbers below to Subtract")
    try:
        userInput = int(input("Enter the first number: "))
        userInput1 = int(input("Enter the second number : "))
        sub = userInput - userInput1
        print("Subtraction: ", sub)
    except ValueError:
        print("Error Message: You can only enter Numbers")

def Division():
    print("Enter the numbers below to Divide")
    try:
        userInput = int(input("Enter the numerator: "))
        userInput1 = int(input("Enter the denominator: "))
        while userInput1 == 0:
            print("Denominator cannot be zero")
            userInput1=int(input("Enter the denominator: "))
        div=userInput / userInput1
        print("Division: ", div)

    except ValueError:
        print("Error Message: You can only enter Numbers")

def Multiplication():
    print("Enter the numbers below to Multiply")
    try:
        userInput = int(input("How many numbers do you want to multiply: "))
        count = 0
        prod = 1
        while count < userInput:
            userInput1 = int(input("Enter the number: "))
            prod = prod * userInput1
            count = count +1
        print("Multiplication: ", prod)
    except ValueError:
        print("Error Message: You can only enter Numbers")

def main():
    while True:
        userChoice = calculator()

        if userChoice == 'ME':
            Menu()
        elif userChoice == 'A':
            Addition()
        elif userChoice == 'S':
            Subtraction()
        elif userChoice == 'D':
            Division()
        elif userChoice == 'MU':
            Multiplication()
        elif userChoice == "Q":
            exit()
        else:
            print("Please choose options only")


main()


