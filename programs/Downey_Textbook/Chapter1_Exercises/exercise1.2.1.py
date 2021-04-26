# This program converts mins to seconds. You can change the mins 
# and secs to any numbers and it should still convert properly

# 1) How many seconds are there in 4.2 minutes 42 seconds?
print("\nMinutes to Seconds Converter\n")

mins = float(input("Enter the initial amount of mins: ")) 
secs = float(input("Enter the initial amount of secs: "))           

#60 secs = 1 min, so multiply mins by 60 and add up additional seconds
totalSeconds = int((mins*60) + secs)    #Rounds to nearest whole #

print("There are", totalSeconds, "secs in", mins, "mins", secs, "secs")

#Answer: There should be 294 secs in 4.2 mins 42 secs