# Question: Print the Score - 3

# Write a program that reads a distance D in km and calculates the total score.

# For the first 20 km (0 - 20 km), the score for each km is 2.
# For the next 40 km (21 - 60 km), the score for each km is 4.
# For the distance above 60 km, the score for each km is 6.
# Apart from the above scores, there is a bonus score of 30.

# The input will be a single line containing an integer representing D. 
# The output should be a single line containing an integer that is the score.

distance = int(input())
bonus = 30
if distance <= 20:
    dis = distance * 2
elif distance <= 60:
    dis = (20 * 2) + ((distance - 20) * 4)
else:
    dis = (20 * 2) + (40 * 4) + ((distance - 60) * 6)
    
total_distance = dis + bonus
print(total_distance)