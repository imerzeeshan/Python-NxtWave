# Write a program to display a customized message based on temperature T.

# Input
# The first line is a real number T.

# Output
# Print Freezing weather if T<0
# Print Very Cold weather if 0<=T<10
# Print Cold weather if 10<T<20
# Print Normal if 20<T<30
# Print Hot if 30 <T<40
# Print Very Hot if T>= 40

# Explanation
# In the given example, the temperature is -50.0.
# As the temperature is less than 0 the output should be Freezing weather

temp = float(input())

if temp < 0:
    print("Freezing weather")
elif temp < 10:
    print("Very Cold weather")
elif temp < 20:
    print("Cold weather")
elif temp < 30:
    print("Normal")
elif temp < 40:
    print("Hot")
else:
    print("Very Hot")