# Solved
# Largest Prime Factor

# Problem 3
# The prime factors of 13195 are 5, 7, 13, 29.
# What is the largest prime facotr of the number 600851475143?
# Answer: 6857


# Solution:

number = 600851475143
factor = []
divisible = 2

while number > 1:
    if number % divisible == 0:
        factor.append(divisible)
        number //= divisible
    else:
        divisible += 1

print(factor[-1])