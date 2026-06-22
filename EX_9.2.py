investmentAmount = float(input("Enter investment amount: "))
annualInterestRate = float(input("Enter annual interest rate (e.g., 5 for 5%): "))
numberOfYears = int(input("Enter number of years: "))

monthlyInterestRate = annualInterestRate / 1200
futureValue = investmentAmount * (1 + monthlyInterestRate) ** (numberOfYears * 12)

print(f"Future value is: ${futureValue:.2f}")