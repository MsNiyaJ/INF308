# This program converts kilometers to miles by dividing the km by 1.61.
# You can change the number of kilometers and it should still convert properly

# 2) How many miles are there in 10 kilometers? 
# Hint: there are 1.61 kilometers in a mile.
print("Kilometers to Miles Converter")
km = input("How many kilometers: ")
km = float(km)               #converts the string to a float
miles = int((km / 1.61))     #converts a float to an int

print("There are", miles, "miles in", km, "kilometers")

#Ans: There should be 6 miles in 10 km.