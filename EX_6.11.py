def computeCommission(salesAmount):
    if salesAmount <= 10000:
        return salesAmount * 0.09
    elif salesAmount <= 50000:
        return 10000 * 0.09 + (salesAmount - 10000) * 0.10
    else:
        return 10000 * 0.09 + 40000 * 0.10 + (salesAmount - 50000) * 0.11

print(f"{'Sales Amount':<20} {'Commission'}")
print("-" * 35)
for sales in range(10000, 100001, 5000):
    commission = computeCommission(sales)
    print(f"{sales:<20} {commission}")