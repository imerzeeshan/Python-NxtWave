# This program is designed to assess a number N against two specific conditions:

# Whether N is divisible by both 5 and 7.
# Whether N is less than 7.

n = int(input())

divisible_5_7 = ((n % 5) == 0) and ((n % 7) == 0)
n_less = n < 7

if divisible_5_7 or n_less:
    print(n)
else:
    print(n % 5)
    print(n % 7)