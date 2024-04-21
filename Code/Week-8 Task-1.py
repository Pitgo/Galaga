class ChildAge:
    def __init__(self, age_str):
        age_list = age_str.split(':')
        self.years = int(age_list[0])
        self.months = int(age_list[1])

    def __str__(self):
        return f"{self.years:02}:{self.months:02}"

    def __lt__(self, other):
        if self.years == other.years:
            return self.months < other.months
        return self.years < other.years

    def __eq__(self, other):
        return self.years == other.years and self.months == other.months


# Collect ages from the user
ages = []
for i in range(3):
    age_input = input(f"Enter the age of the child {i + 1} in the format (age: months) ")
    ages.append(ChildAge(age_input))

# Find the youngest person's age
youngest = min(ages)

# Output the youngest person's age
print(f"The youngest person's age is {youngest.years} years and {youngest.months} months")