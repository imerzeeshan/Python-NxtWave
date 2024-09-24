#Write a program that reads the attendance percentage A and status of having medical report M of a student and checks if any of the below conditions is satisfied.
# A is greater than or equal to 75.
# M is equal to "Y".
# Print Allowed to write exam if any of the given conditions is satisfied. Otherwise, print Cannot write exam.

# Note
# The last character of the attendance percentage A contains %.
# The remaining characters contain a Number.

# Example: 40%, 60%

# Input
# The first line of input contains a string representing A The second line of input contains a string representing M




a = input()
medical_reason = input()
ln = len(a)

per = int(a[:ln-1])

if per >= 75 :
    print("Allowed to write exam")
elif per < 75 and medical_reason == "Y":
    print("Allowed to write exam")
else:
    print("Cannot write exam")