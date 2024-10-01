# Write a program that reads two numbers A and B, and checks if A2 + B 2 (sum of the square of A and the square of B) is greater than or equal to 60.

# Print Greater than or Equal to 60 if the sum of the square of A and the square of B is greater than or equal to 60. Otherwise, print Less than 60.

a = int(input())
b = int(input())

sum_of_square = (a ** 2) + (b ** 2)

if sum_of_square >= 60:
    print("Greater than or Equal to 60")
else:
    print("Less than 60")