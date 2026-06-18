def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for n in range(2, 999):
    if isPrime(n) and isPrime(n + 2):
        print(f"({n}, {n + 2})")