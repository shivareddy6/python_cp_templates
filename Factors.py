from collections import defaultdict

def get_prime_factors(n):
    d = defaultdict(int)
    fact = 2
    while fact*fact <= n:
        while (n%fact == 0):
            d[fact] += 1
            n //= fact
        fact += 1
    if n > 1:
        d[n] += 1
    return d

def getFactors(n):
    factors = []
    i = 1
    while i*i < n:
        if n%i == 0:
            factors.append(i)
            factors.append(n//i)
        i += 1
    if i*i == n:
        factors.append(i)
    return factors

print(sorted(getFactors(16)))