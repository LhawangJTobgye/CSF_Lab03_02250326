def multiplication_table(num):
    print("Multiplication Table of", num)
    for x in range(1, 13):
        print(num, "x", x, "=", num * x)

n = int(input("Enter a number: "))
multiplication_table(n)