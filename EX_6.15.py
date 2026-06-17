def computeTax(status, taxableIncome):
    # Tax brackets: [upper_limit, rate]
    brackets = {
        0: [(8350, 0.10), (33950, 0.15), (82250, 0.25), (171550, 0.28), (372950, 0.33), (float('inf'), 0.35)],   # Single
        1: [(16700, 0.10), (67900, 0.15), (137050, 0.25), (208850, 0.28), (372950, 0.33), (float('inf'), 0.35)],  # Married Joint
        2: [(8350, 0.10), (33950, 0.15), (82250, 0.25), (171550, 0.28), (372950, 0.33), (float('inf'), 0.35)],    # Married Separate
        3: [(11950, 0.10), (45500, 0.15), (117450, 0.25), (190200, 0.28), (372950, 0.33), (float('inf'), 0.35)],  # Head of House
    }

    tax = 0
    prev_limit = 0
    for limit, rate in brackets[status]:
        if taxableIncome <= prev_limit:
            break
        taxable = min(taxableIncome, limit) - prev_limit
        tax += taxable * rate
        prev_limit = limit

    return int(tax)

# Print table header
print(f"{'Taxable':<10} {'Single':<10} {'Married':<10} {'Married':<10} {'Head of'}")
print(f"{'Income':<10} {'':10} {'Joint':<10} {'Separate':<10} {'a House'}")
print("-" * 50)

for income in range(50000, 60001, 50):
    s0 = computeTax(0, income)
    s1 = computeTax(1, income)
    s2 = computeTax(2, income)
    s3 = computeTax(3, income)
    print(f"{income:<10} {s0:<10} {s1:<10} {s2:<10} {s3}")