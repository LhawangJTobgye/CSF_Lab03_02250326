def even_odd_till(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i, "is Even")
        else:
            print(i, "is Odd")

n = int(input("Enter a number: "))
even_odd_till(n)

# Loops from 1 to n. #
# Checks even/odd using % 2. #
# Prints each number with its own status. #