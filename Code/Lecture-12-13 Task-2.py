def emi_calculation(p, r, n):
    emi = p * r * ((1 + r) ** n) / (((1 + r) ** n) - 1)
    return emi



try:
    p = float(input("Enter the principal loan amount: "))
    r = float(input("Enter the rate of interest (in decimal): "))
    n = int(input("Enter the duration of the loan (in months): "))

    monthly_repayment = emi_calculation(p, r, n)
    print("Monthly repayment: {:.2f}".format(monthly_repayment))

except ValueError:
    print("Invalid input. Please enter numeric values.")