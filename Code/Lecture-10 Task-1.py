x = int(input("Enter a positive value: "))

if x < 0:
    print("Value entered is not positive")
else:
    reversed = bin(x)[::-1]
    reversed = reversed[:-2]
    print(reversed)