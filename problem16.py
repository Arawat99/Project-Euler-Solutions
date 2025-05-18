# Solved
# Power Digit Sum

# Problem 16
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26
# What is the sum of the digits of the number 2^1000?
# Answer: 1366

# Solution:

num = 1
sum = 0

for i in range(1000):
    num *= 2

while num > 0:
    a = num % 10
    num //= 10
    sum += a

print(sum)
