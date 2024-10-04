# This program determines the behavior of an integer N based on its divisibility by 3. It performs two primary functions:

# Checks if N is divisible by 3.
# Based on the divisibility, it either triples N if it is divisible by 3 or doubles N if it is not.

n = int(input())

divisible = (n % 3) == 0

if divisible:
    print(n * 3)
else:
    print(n * 2)