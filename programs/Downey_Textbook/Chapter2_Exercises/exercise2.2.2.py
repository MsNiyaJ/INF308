# 2) Suppose the cover price of a book is $24.95, 
# but bookstores get a 40% discount. Shipping costs
# $3 for the first copy and 75 cents for each additional 
# copy. What is the total wholesale cost for 60 copies?

print("\nCalculate the Wholesale Cost")

#Makes sure the following inputs are numeric before conversion
while True:
    try:
        ogPrice = float(input("What is the price of the book?: $"))
        discount = float(input("Enter a discount by percent(%): "))
        numOfCopies = int(input("How many copies do you want?: "))
        break
    except ValueError:
        print("\nInvalid entry. Try again.")

discount = discount / 100     #convert whole number to decimal

#Determine the discounted price of the book before shipping
dP = ogPrice - (ogPrice*discount)

shippingCosts = .75
numOfCopies = 60

# Loops until the user gets at least one copy.
while(numOfCopies < 1):
    print("\nMust enter a number greater than 0.")
    numOfCopies = input("How many copies do you want?: ")

    #Makes sure the string is a number before converting it to an int
    if(numOfCopies.isnumeric()):
        numOfCopies = int(numOfCopies)      #Converts string to int
    else:
        print("Invalid input")
        numOfCopies = -1


# Add $3 to the discounted price for the first copy and 
# add 75 cents for each additional copy.
if(numOfCopies == 1):
    wholesalePrice = dP + 3       
elif(numOfCopies > 1):
    wholesalePrice = dP + 3 + (numOfCopies - 1)*shippingCosts        


wholesalePrice = round(wholesalePrice, 2)     #rounds to two decimal places
wholesalePrice = "$"+ str(wholesalePrice)     #Converts to string and concatenates a $

print("\nThe wholesale price is", wholesalePrice)

#Answer: The wholesale price is $62.22