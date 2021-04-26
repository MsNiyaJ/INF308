# The following program reads a file that contains messages,
# counts how many times each person sent a message, then
# prints out the email of the person who has the most commits.

# Created a dictionary that will act as a counter 
counter = dict()


# Opens a file and if the file doesn't exist, end the program
def openFile(filename):
    
    try:
        file = open(filename)        # Opens a file
        return file
    except (FileNotFoundError, IOError):
        print("File not found. Exiting program...")
        exit()                       # Ends the program

    # print(file.read(4))    #TEST: Checking to see if the file opened. SHOULD PRINT THE WORD "File"

# Counts the number of messages that each person sent and stores it in the counter dictionary
def countMessages(file):
    # Loops through each line in the file
    for line in file:
        
        # If the line has the word "From", split the line into a list called words
        if "From:" in line:
            words = line.split()
            
            # For each word in the list, check if there is an @ symbol
            for word in words:

                # If the @ symbol exists in the word, store the email address in the counter
                if "@" in word:
                    # print(word)      # Prints each email address 
                    if word not in counter:
                        counter[word] = 1
                    else:
                        counter[word] += 1

#Stores a new tuple in a list that will set the number of messages as the key, and the email address as the value
def addValuesToList(lst):
    
    # Loops through a list of tuples and adds a new tuple to a new list
    for key, value in list(counter.items()):
        lst.append((value, key)) 

# Returns the email and key of the first person in the list 
def getPersonWithMostCommits(lst):
    for key, value in lst:
        
        personWithMostCommits = str(value)+" has the most commits! ("+str(key)+")"
        return personWithMostCommits


def main():
    # Prompt user to enter a file
    fname = input("Enter a file name:\n> ")
    file = openFile(fname)
    countMessages(file)
    
    lst = list()                #Creates a new list
    addValuesToList(lst)
 
    lst.sort(reverse=True)                 #Sorts the list in descending order       
    personWithMostCommits = getPersonWithMostCommits(lst)  #String containing the person with the most commits
    
    print(personWithMostCommits)
    
    # In 'mbox-short.txt' output should be: "cwen@iupui.edu has the most commits! (5)"
    # In 'mbox.txt' output should be: "zqian@umich.edu has the most commits! (195)"

main()
