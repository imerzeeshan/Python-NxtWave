# Write a program that reads an operator O, and two numbers A and B.

# Print the result by doing arithmetic operations on A and B based on the operator O.

# Operator	Arithmetic Operation	Represents
#    +	   |         A + B	      |  Addition of A and B
#    -	   |         A - B	      |  Subtraction of B from A
#    *	   |         A * B	      |  Multiplication of A and B
#    /	   |         A / B	      |  Division of A and B
#    %	   |         A % B	      |  Remainder when A is divided by B


operator = input()
a = int(input())
b = int(input())

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    print(a / b)
elif operator == "%":
    print(a % b)