# The program is intended to calculate the hypotenuse H of a right-angled triangle, given the lengths of the two other sides, A and B. The hypotenuse is the side opposite the right angle in a right-angled triangle and can be calculated using Pythagoras's theorem. 
# Logical Approach:

# Read Input:
# Read the lengths of the sides A and B as integers.

# Calculate the Hypotenuse:
# Apply Pythagoras's theorem, which states that in a right-angled triangle, the square of the hypotenuse (H) is equal to the sum of the squares of the other two sides (A and B). This can be represented as H = (A^2 + B^2)^0.5.

# Output:
# Compute the value of H using the formula and then convert it to an integer. This step is necessary as the square root of a sum of squares might not always be an integer, but the question specifies the output should be an integer.
# Print the value of the hypotenuse H.

# Example for Clarity:

# If the input sides A and B are 3 and 4, respectively:
# The square of A is 3^2 = 9.
# The square of B is 4^2 = 16.
# The sum of the squares of A and B is 9 + 16 = 25.
# The hypotenuse H is the square root of 25, which is 5. Therefore, the output is 5.
# The output will be: 5




a = int(input())
b = int(input())

hy = int(((a ** 2) + (b ** 2)) ** 0.5)

print(hy)