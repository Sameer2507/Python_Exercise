import re

ssn = input("Enter a Social Security number (ddd-dd-dddd): ")
if re.fullmatch(r"\d{3}-\d{2}-\d{4}", ssn):
    print("Valid SSN")
else:
    print("Invalid SSN")