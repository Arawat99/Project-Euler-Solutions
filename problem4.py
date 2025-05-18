# Solved
# Finding Largest Palindrome Product

# Problem 4
# A palindrome number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
# Answer: 906609


# Solution:

largestPalindrome = 0
found = False

def check(num1, num2):
    product = num1 * num2
    palindrome = product
    reversePalindrome = 0

    while palindrome > 1:
        reversePalindrome *= 10
        remainder = palindrome % 10
        reversePalindrome += remainder
        palindrome //= 10
    
    if product == reversePalindrome:
        return True
    return False

for num1 in range(1000, 900, -1):
    for num2 in range(1000, 900, -1):
        if check(num1, num2):
            largestPalindrome = num1 * num2
            found = True
            break
    if found:
        break

print(largestPalindrome)