class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        return

    def PrintAttributes(self):
        print(f"The person {self.name}'s age is {self.age}, salary is {self.salary}")

Joe = Person("Joe", 25, 5000)
John = Person("John", 25, 4000)
Grayson = Person("Grayson", 25, 4000)

Joe.PrintAttributes()
John.PrintAttributes()
Grayson.PrintAttributes()