

n = int(input("Enter the Number: "))
if n % 2 == 0:
    print("Number is even")
    if n >= 2 and n <= 5:
        print("Not weird")
    elif n > 5 and n < 21:
        print("Weird")
    elif n > 20:
        print("Not weird")
else:
    print("Number is odd and weird")



