# Write a program to print the smallest value among the three numbers A Band C.

# Input
# The first line is an integer A
# The second line is an integer B
# The third line is an integer C

# Explanation
# In the given values A6 B5, C44 is the smallest value among the three. So the output should be 4.

a = int(input())
b = int(input())
c = int(input())

if a < b:
    if a < c:
        print(a)
    else:
        print(c)
else:
    if b < c:
        print(b)
    else:
        print(c)