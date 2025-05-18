# Solved
# Factorial Digit Sum

# n! means n x (n - 1) x ... x 3 x 2 x 1.
# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!.
# Answer: 648

# Solution:

number = 1
sum = 0

for i in range(1, 101):
    number *= i

while number > 0:
    digit = number % 10
    number //= 10
    sum += digit

print(sum)