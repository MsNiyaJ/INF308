# A program that prints 'Hello Person' 
# until they enter the word 'Quit'

while True:
    print("\nHello Person! :)\n")
    msg = input("Enter the word \'Quit\' to end the program...\n> ")
    
    # Changes the input to lowercase letters
    msgToLower = msg.lower()

    # Ends the program if a user enters 'Quit'    
    if msgToLower == "quit":
        break

    # Prints the users input
    print("You responded: \'"+msg+"\'")

