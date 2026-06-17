def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):
    return investmentAmount * (1 + monthlyInterestRate) ** (years * 12)

investmentAmount = float(input("Enter investment amount: "))
annualRate = float(input("Enter annual interest rate (e.g. 5 for 5%): "))
monthlyInterestRate = annualRate / 100 / 12

print(f"\n{'Years':<10} {'Future Value':>15}")
print("-" * 25)
for years in range(1, 31):
    futureValue = futureInvestmentValue(investmentAmount, monthlyInterestRate, years)
    print(f"{years:<10} {futureValue:>15.2f}")