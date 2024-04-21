name = str(input("Write your name (Name MiddleName(Optional) LastName): "))

names = name.split(" ")

if len(names) == 3:
    print(f"Hello {names[2]}, {names[0][0]}.{names[1][0]}.!")
elif len(names) == 2:
    print(f"Hello {names[1]}, {names[0][0]}.!")