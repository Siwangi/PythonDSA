def factorial(k):
    count = 0
    prod = 1
    while count < k:
        prod = prod * (k-count)
        count = count + 1
    print("factorial: ", prod)
    return prod

factorial(6)