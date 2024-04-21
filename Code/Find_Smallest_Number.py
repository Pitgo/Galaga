def find_smallest(numbers):
    if not numbers:
        return None
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

numbers = [5, 3, 8, 1, 9, 2]
smallest_number = find_smallest(numbers)
print("The smallest number is:", smallest_number)
