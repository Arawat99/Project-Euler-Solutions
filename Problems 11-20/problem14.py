# Solved
# Longest Collatz Sequence

# Problem 14
# The following iterative sequence is defined for the set of positive integers:

# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)


# Using the rule above and starting with 13, we generate the following sequence:

# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1.

# It can be seen that this sequence (starting at 13 and finishing at 1) contains
# 10 terms. Although it has not been proved yet (Collatz Problem), it is thought
# that all starting numbers finish at 1.


# Which starting number, under one million, produces the longest chain?
# Note: Once the chain starts the terms are allowed to go above one million.

# Answer: 837799

# Brute Force Method
# Solution:

def sequenceCounter(num, count = 1):
    if num == 1:
        return count
    
    elif num % 2 == 0:
        return sequenceCounter(num // 2, count + 1)
    else:
        return sequenceCounter((3 * num) + 1, count + 1)


longestchain = 0
startingNumber = 0

for x in range(1000000, 0 , -1):
    currentChain = sequenceCounter(x)

    if longestchain < currentChain:
        longestchain = currentChain
        startingNumber = x
        
        print("Currently Highest Chain Number: " + str(startingNumber) + ", Number of Chain: " + str(longestchain))


print("Number with the Longest Chain:" + str(startingNumber))
print("Number of Chain: " + str(longestchain))