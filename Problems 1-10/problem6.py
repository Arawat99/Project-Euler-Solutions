# Solved
# Sum Square Difference

# Problem 6
# The sum of the squares of the first ten natural numbers is,

# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)^2 = 55^2 = 3025.
# Hence the difference between the sum of the squares of the first ten natural
# nummbers and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.
# Answer: 25164150

# Solution:

sumOfTheSquaresOfTheFirstTenNaturalNumbers = 0
squareOfTheSumOfTheFirstTenNaturalNumbers = 0
sum = 0

for num in range(101):
    product = num * num
    sumOfTheSquaresOfTheFirstTenNaturalNumbers += product
    sum += num

squareOfTheSumOfTheFirstTenNaturalNumbers = sum * sum
print(squareOfTheSumOfTheFirstTenNaturalNumbers - sumOfTheSquaresOfTheFirstTenNaturalNumbers)