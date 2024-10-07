# The program is designed to check if a given number N is not divisible by any of the numbers 2, 3, 5, and 7. 



n = int(input())

divisible_2 = (n % 2) != 0
divisible_3 = (n % 3) != 0
divisible_5 = (n % 5) != 0
divisible_7 = (n % 7) != 0

ans = divisible_2 and divisible_3 and divisible_5 and divisible_7

print(ans)