# Question: Sum of The Digits - 2

# Given an integer between 0 and 10000, write a program to print the sum of its digits. 
# For example, if the given number is 25, your code should print the sum of the digits (2 + 5), 
# which is 7. Similarly, if the given number is 692, your code should print the sum of the digits (6 + 9 + 2), 
# which is 17. If the given number is 9999, 
# your code should print the sum of the digits (9 + 9 + 9 + 9), which is 36.


num = input()
length = len(num)

if length == 1:
    print(int(num[0]))
elif length <= 2:
    print(int(num[0]) + int(num[1]))
elif length <= 3:
    print(int(num[0]) + int(num[1]) + int(num[2]))
elif length <= 4:
    print(int(num[0]) + int(num[1]) + int(num[2]) + int(num[3]))
elif length <= 4:
    print(int(num[0]) + int(num[1]) + int(num[2]) + int(num[3]) + int(num[4]))
