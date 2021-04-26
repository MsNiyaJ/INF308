# 3) If you run a 10 kilometer race in 42 minutes 42 seconds, 
# what is your average pace (time permile in minutes and seconds)? 
# What is your average speed in miles per hour?

km = 10
imins = 42      #initial mins
isecs = 42      #initial secs

#Convert km to miles (1.61 miles = 1 km)
miles = km / 1.61

# Convert the secs to minutes and adds up the 
# total amount of mins (1 min = 60 secs)
totalMins = imins + (isecs / 60)

# Calculates the average pace (time per mile) 
averagePace = totalMins / miles

#Converts the average pace (in mins) back to mins and secs
mins = int(averagePace)     
secs = int((averagePace - mins) * 60)       

print("Pace per mile:", mins, "mins and", secs)

#Calculates the speed in miles per hour (speed = distance/time)
averageSpeed = int(miles / (totalMins / 60))    # miles / hours
print("Speed:", averageSpeed, "mph") 