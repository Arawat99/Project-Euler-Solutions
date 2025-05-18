# Solved
# Smallest Multiple

# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of
# the numbers from 1 to 20?
# Answer: 232792560


numbers = [n for n in range(1, 21)]

def gcd(num1, num2):
    if num2 == 0:
        return num1
    return gcd(num2, num1 % num2)

def lcm(num1, num2):
    product = num1 * num2
    return product // gcd(num1, num2)

def smallest_multiple(number):
    it = iter(number)
    a = next(it)

    for num in number:
        a = lcm(a, num)

    return a

# Similar Solution
# def smallest_multiple(number):
#     it = iter(number)
#     a = next(it)

#     while True:
#         try:
#             a = lcm(a, next(it))
#         except StopIteration:
#              break
#     return a

print(smallest_multiple(numbers))