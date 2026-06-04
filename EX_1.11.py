population = 312032486
seconds_in_year = 365 * 24 * 60 * 60

births_per_year = seconds_in_year // 7
deaths_per_year = seconds_in_year // 13
immigrants_per_year = seconds_in_year // 45

population = population + births_per_year - deaths_per_year + immigrants_per_year
print(f"Year 1: {population}")

population = population + births_per_year - deaths_per_year + immigrants_per_year
print(f"Year 2: {population}")

population = population + births_per_year - deaths_per_year + immigrants_per_year
print(f"Year 3: {population}")

population = population + births_per_year - deaths_per_year + immigrants_per_year
print(f"Year 4: {population}")

population = population + births_per_year - deaths_per_year + immigrants_per_year
print(f"Year 5: {population}")