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
    print("Enter number to Add")
    userInput = int(input("Enter the number to add: "))
    sum = userInput + userInput
    print("Addition: ", sum)


def Subtraction():
    print("Enter number to Subtract")
    userInput = int(input("Enter the number to add: "))
    sub = userInput - userInput
    print("Subtraction: ", sub)

def Division():
    print("Enter number to Divide")
    userInput = int(input("Enter the number to add: "))
    div = userInput / userInput
    print("Division: ", div)

def Multiplication():
    print("Enter number to Multiply")
    userInput = int(input("Enter the number to add: "))
    prod = userInput * userInput
    print("Multiplication: ", prod)

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


main()


