# Write a program that reads a two-digit number N and checks if any of the given conditions is satisfied.
# • The number N is divisible by 9.
# • One of the digits of the number N is equal to 9.
# Print Lucky Number if any of the given conditions is satisfied. Otherwise, print Unlucky Number.


n = input()

digit_9 = (int(n[0]) == 9) or (int(n[1]) == 9)

n = int(n)

divisible_9 = ((n % 9) == 0)

if divisible_9 or digit_9:
    print("Lucky Number")
else:
    print("Unlucky Number")