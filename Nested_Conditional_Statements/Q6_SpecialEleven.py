# Write a program that reads a number N and checks if the remainder is 0 or 1 when N is divided by 11.
# Print Special Eleven if the remainder is 0 or 1 when N is divided by 11. Otherwise, print Normal Number.

n = int(input())

remainder = ((n % 11) == 0) or ((n % 11) == 1)

if remainder:
    print("Special Eleven")
else:
    print("Normal Number")