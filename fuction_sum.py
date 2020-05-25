# Applebees
# 15 - Division

def main():
    anthony_benigno={"Atlantic City": 50, "Mays Landing": 58, "Somers Point": 84, "Turnersville": 86,
                     "Williamstown": 68}

    print(Adoption_Rate(anthony_benigno))
    print(Average(anthony_benigno))


def Adoption_Rate(anthony_benigno):
    sum = 0
    for store in anthony_benigno:
        sum = sum + anthony_benigno[store]

    return sum



def Average(anthony_benigno):
    sum = 0
    count = 0
    for store in anthony_benigno:
        sum=sum + anthony_benigno[store]
        count = count + 1

    return (sum/count)





main()

