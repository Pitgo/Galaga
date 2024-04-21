x = int(input("Enter 1st value: "))
y = int(input("Enter 2nd value: "))

i = x

if x <= y:
    print(i)
    while x + 5 <= y:
        i += 5
        full_str += (str(i) + " ")

        if i >= y:
            print(full_str)
            break
else:
    print("1st value most be less than 2nd value")