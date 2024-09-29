# The program is tasked with determining whether a given year Y is a leap year 
# based on two specific conditions:

# The year Y is divisible by 400.
# The year Y is divisible by 4, but not divisible by 100.
# The program should output True if either of these conditions is met, 
# indicating that the year is a leap year. 
# If neither condition is satisfied, the program should output False.

y = int(input())

if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 == 0:
            print("True")
        else:
            print("False")
    else:
        print("True")
else:
    print("False")