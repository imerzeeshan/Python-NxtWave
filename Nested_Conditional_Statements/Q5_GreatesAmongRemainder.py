# Write a program that reads a number N and finds the,
# • Remainder when N is divided by 4.
# • Remainder when N is divided by 5.
# Print the greatest remainder among the two remainders when N is divided by 4 and 5.


n = int(input())

divided_by_4 = n % 4
divided_by_5 = n % 5

if divided_by_4 > divided_by_5:
    print(divided_by_4)
else:
    print(divided_by_5)