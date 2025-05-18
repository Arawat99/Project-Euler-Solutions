# Solved
# Summation of Primes

# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
# Find the sum of all the primes below two million
# Answer: 142913828922


# Solution:

import math

def isPrime(Number):
    if Number == 1:
        return False
    elif Number < 4:
        return True
    elif Number % 2 == 0:
        return False
    elif Number < 9:
        return True
    elif Number % 3 == 0:
        return False
    else:
        root = int(math.sqrt(Number))
        f = 5
        while f <= root:
            if Number % f == 0:
                return False
            if Number % (f + 2) == 0:
                return False
            f += 6
        return True

sum = 0

for i in range(2000000):
    if isPrime(i):
        sum += i

print("Total Sum: ", sum)