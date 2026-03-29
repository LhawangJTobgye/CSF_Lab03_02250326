a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if a > b:
    if a > c:
        print("The largest number is:", a)
    else:
        print("The largest number is:", c)
else:
    if b > c:
        print("The largest number is:", b)
    else:
        print("The largest number is:", c)

# Compares a with b first. #
# Then compares the larger of a and b with c to find the largest. #
 #Uses nested if-else for stepwise comparison. #