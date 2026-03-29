numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
search = int(input("Enter the number to search: "))

for num in numbers:
    if num == search:
        print("Number found:", num)
        break
else:
    print("Number is not found in the list.")