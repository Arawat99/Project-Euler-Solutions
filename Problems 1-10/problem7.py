# Solved
# 10 0001st prime factor

# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.

# What is the 10 001st prime number?
# Answer: 104743

# Solution:

import math
count = 0
num = 1

def isPrimeNumber(Number):
    squareRoot = int(math.sqrt(Number))
    for i in range(2, squareRoot + 1):
        if Number % i == 0:
            return False
    return True

# Using Sieve of Erathosthene
# More Efficient in larger numbers due to smaller number of iterations and reducing number of checks
# def isPrime(Number):
#     if Number == 1:
#         return False
#     elif Number < 4:
#         return True
#     elif Number % 2 == 0:
#         return False
#     elif Number < 9:
#         return True
#     elif Number % 3 == 0:
#         return False
#     else:
#         root = int(math.sqrt(Number))
#         f = 5
#         while f <= root:
#             if Number % f == 0:
#                 return False
#             if Number % (f + 2) == 0:
#                 return False
#             f += 6
#         return True
    
while not count == 10001:
    num += 1
    if isPrimeNumber(num):
        count += 1

print(f"Number {num} is 10001st Prime Number")