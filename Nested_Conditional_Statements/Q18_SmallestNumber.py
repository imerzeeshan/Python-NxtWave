# This program calculates the remainders of two different divisions involving two numbers A and B, and then identifies the smaller of the two remainders. The two key operations are:

# Calculating the remainder when A is divided by B (A % B).
# Calculating the remainder when B is divided by A (B % A).
# The smallest of these two remainders is then printed as the output.

a = int(input())
b = int(input())

a_divisible_b = a % b
b_divisible_a = b % a

if a_divisible_b > b_divisible_a:
    print(b_divisible_a)
else:
    print(a_divisible_b)