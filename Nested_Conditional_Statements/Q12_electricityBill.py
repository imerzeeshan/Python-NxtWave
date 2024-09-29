# In this problem, you need to write a program to calculate the electricity bill for a household, based on the units of electricity the household consumed. The price for unit varies based on the slab. The charges per unit for different slabs are as mentioned below:
# For the first 50 units (0-50), the charge is 2/unit
# For the next 100 units (51-150), the charge is 3/unit
# For the next 100 units (151-250), the charge is 5/unit
# For above 250 units (251 and above), the charge is 8/unit
# Apart from these charges, there is also an additional surcharge of 20% on the total amount is added to the bill.



u = int(input())

if u <= 50:
    bill = (u * 2)
elif u <= 150:
    bill = (50 * 2) + ((u - 50) * 3)
elif u <= 250:
    bill = (50 * 2) + (100 * 3) + ((u - 150) * 5)
else:
     bill = (50 * 2) + (100 * 3) + (100 * 5) + ((u - 250) * 8)

gst = bill * 0.2
total_bill = gst + bill

print(total_bill)