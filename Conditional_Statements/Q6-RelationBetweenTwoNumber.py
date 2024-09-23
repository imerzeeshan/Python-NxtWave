# Write a program to print the relation between two numbers, A and B.

# Input
# The first line is an integer A
# The second line is an integer B

# Output
# Print AB if A and B are equal.
# Print AB If A is greater than B.
# Print AB if A is less than B.

# Explanation
# Given A = 3, B = 4
# As 3 < 4, the output should be A < B.

a = int(input())
b = int(input())

if a == b:
    print("A == B")
elif a > b:
    print("A > B")
else:
    print("A < B")