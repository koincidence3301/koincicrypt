import re

def isprime(n):
    return re.compile(r'^1?$|^(11+)\1+$').match('1' * n) is None
primes = [x for x in range(3307) if isprime(x)]

