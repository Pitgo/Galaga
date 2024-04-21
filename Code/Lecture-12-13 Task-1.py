numbers = []

def get_numbers(amount):
    for i in range(amount):
        numbers.append(int(input(f"{i + 1}. ")))

def print_odd_numbers(list):
    print("This are all the odd numbers in your list:")
    for i in range(len(list)):
        if (list[i] % 2 != 0):
            print(f"{list[i]}")

def print_even_numbers(list):
    print("This are all the even numbers in your list:")
    for i in range(len(list)):
        if (list[i] % 2 == 0):
            print(f"{list[i]}")

def print_all_numbers(list):
    print("This are all the numbers in your list:")
    for i in range(len(list)):
        print(f"{list[i]}")

get_numbers(int(input("How many numbers you want to enter: ")))
print()
print_odd_numbers(numbers)
print()
print_even_numbers(numbers)
print()
print_all_numbers(numbers)

