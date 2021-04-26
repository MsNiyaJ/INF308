# Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. 
# Ask the user to enter a regular expression and count the number of lines that matched the regular expression

import re

def openFile(filename):
    print(filename)

    # Reads a file and returns it
    # Displays an error message and exits the program if the file was not found
    try:
        file = open(filename, 'r')        
        return file
    except (FileNotFoundError, IOError) as err:
        print(err, "\nCheck your path and filename. Exiting program...")
        exit()    

def count(regex, file):
    count = 0       # counter for the number of times the regex was found in the file

    # Loop through each line, strip white space, 
    # and add 1 to the counter each time the regex is found in a line
    for line in file:
        line = line.rstrip()
        if re.findall(regex, line):
            count += 1

    return count

def main():
    path = 'C:\\Users\\Owner\\Documents\\UAlbany\\Spring21\\INF308\\Github\\inf308fall2020-MsMalcolm\\programs\\Severance_Textbook\\Chapter11_Exercises\\'
    fname = 'mbox.txt'
    f = path + fname                # Concatenated the path and filename
    file = openFile(f)

    regex = input('\nEnter a regular expression: \n> ')
    n = count(regex, file)         # The number of lines that matched the given regex
    print(fname, 'had', n, 'lines that matched', regex)    

main()

# RESULTS SHOULD BE:
# mbox.txt had 1798 lines that matched ^Author
# mbox.txt had 14368 lines that matched ^X-
# mbox.txt had 4175 lines that matched java$