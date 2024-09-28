# Write a program that reads a two-digit number N and checks if N is divisible by both the digits of N
# Print the double of N if N is divisible by both the digits of N Otherwise, print N.

n = input()

digit_1 = int(n[0])
digit_2 = int(n[1])

n = int(n)

divisible = ((n % digit_1) == 0) and ((n % digit_2) == 0)

if divisible:
    print(n * 2)
else:
    print(n)