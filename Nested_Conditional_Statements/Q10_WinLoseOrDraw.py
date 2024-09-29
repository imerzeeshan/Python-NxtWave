# Write a program that reads the two scores A and B and compares A with the B.
# Print Win if A is greater than B
# Print Draw if A is equal to B
# Print Lose if A is less than B

a = int(input())
b = int(input())

if a > b:
    print("Win")
elif a == b:
    print("Draw")
else:
    print("Lose")