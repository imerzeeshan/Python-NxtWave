# Write a program to find season for the given month number.

# Input
# The first line of input will contain an integer that indicates the number of the month.
# If the given number of the month is 3, that indicates March month.

# Output
# If the given month is either November or December or January, print "Winter"
# If the given month is either February or March, print "Spring". If the given month is either April or May or June print "Summer",
# If the given month is either July or August, print "Rainy". If the given month is either September or October, print "Autumn",

# Explanation
# For example, if the given month is 1, which indicates January month, the output should be "Winter".
# Similarly, if the given month is 4, which indicates April month, the output should be "Summer".

month = int(input()) #Enter a month number

if (month == 1) or ((month >= 11) and (month <= 12)):
    print("Winter")
elif ((month >= 2) and (month <= 3)):
    print("Spring")
elif ((month >= 4) and (month <= 6)):
    print("Summer")
elif ((month >= 7) and (month <= 8)):
    print("Rainy")
elif ((month >= 9) and (month <= 10)):
    print("Autumn")