# Write a program that reads the marks M of a student and checks,
# • If M is greater than or equal to 90.
# • If M is greater than or equal to 50 but not greater than or equal to 90
# Print Discount is 200 if M is greater than or equal to 90.
# Print Discount is 100 if M is greater than or equal to 50 but not greater than or equal to 90.
# Print No Discount if M is not greater than or equal to 50.


m = int(input())

if m >= 90:
    print("Discount is 200")
elif m >= 50:
    print("Discount is 100")
else:
    print("No Discount")