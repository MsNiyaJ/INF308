# This program calculates the volume of a sphere 
# given a radius


# 1)The volume of a sphere with radius r is (4/3)π(r^3). 
# What is the volume of a sphere with radius 5?

print("\nVolume of a Sphere Calculator")
r = input("Enter a radius: ");      #radius
r = float(r)                        #Convert string to float
pi = 3.1415926535897932
volume = (4/3)*pi*(r**3)            #volume of a sphere
volume = round(volume, 2)           #round to the 2nd decimal point

print("The volume of a sphere with radius", r, "is", volume)

#Answer should be "The volume of a sphere with radius 5 is 523.6"