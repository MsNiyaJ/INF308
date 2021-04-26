# The following program is a tool for handling bibliographies in APA (7th Edition).

# Basic format for books in APA:
# Author, A. A. (Year of publication). Title of work: Capital letter also for subtitle. Publisher Name.

# Basic format for articles in APA:
# Author, A. A. (Year). Title of article. Name of journal, volume number(issue number)

from datetime import date       # Class that get's today's date

bibliographies = list()     # A global list of strings that will be saved to a file

class Book:

    # Initializes the values needed in APA (7th Edition) 
    def __init__(self):
        self.firstname = ''
        self.lastname = ''
        self.book_title = ''
        self.year_published = ''
        self.publisher = ''

    # Gets the information about the book
    def getInfo(self, questions):
        
        bibInfo = list()        # A list of all the info in the bibliography

        # Loops until a user responds to the prompt        
        for question in questions:
            while True: 
                response = input('\n' + question + '\n> ')
                
                # For the year prompt, if the user enters a valid year, add it to bibInfo, else add 'n.d.'
                if 'year' in question: 
                    todays_date = date.today()
                    this_year = todays_date.year        # Gets today's year
                    
                    # If the year is a digit and the year is between 1-2021, add it to bibInfo
                    if(response.isdigit() and int(response) in range(1, this_year+1)):         
                        bibInfo.append(response)
                        break
                    else:
                        print("Invalid year entered...setting year to n.d.")
                        bibInfo.append('n.d.')
                        break
                
                elif(response == ''):                       # If the user's input is empty, display a message
                    print("The input can not be empty.")
                
                # If the question has the word 'number' and the user's entry is a digit, add the response to bibInfo
                elif ('number' in question):
                    if(response.isdigit()):
                        bibInfo.append(response)
                        break
                    else: 
                        print('Invalid number entered.')

                else:
                    bibInfo.append(response)                # Add the user's input to bibInfo
                    break

        return bibInfo

    # Formats the bibliography of the book and returns it.
    # Strips trailing and leading whitespace and capitalizes the first letter of each word
    def formatBibliography(self):

        name = (self.lastname + ', ' + self.firstname[0] + '.').title().strip()
        book_title = (self.book_title + '.').title().strip()

        bibliography = (name + " (" + self.year_published + "). " + book_title + ' ' + self.publisher + '.').strip()
        
        return bibliography

# Article inherits Book class
class Article(Book):
    
    def __init__(self):
        super().__init__()          # Inheriting __init__ from Book class
        self.article_title = ''
        self.journal = ''
        self.volume_number = ''
        self.issue_number = ''
    
    def getInfo(self, questions):
        bibInfo = super().getInfo(questions)        # Calling getInfo(questions) from Book class
        return bibInfo

    # Formats the bibliography of the article and returns it.
    # Strips trailing and leading whitespace and capitalizes the first letter of each word
    def formatBibliography(self):
        name = (self.lastname + ', ' + self.firstname[0] + '.').title().strip()
        article_title = (self.article_title + '.').title().strip()
        journal = (self.journal + ',').title().strip()

        bibliography = (name + " (" + self.year_published + "). " + article_title + ' ' + journal + ' ' + self.volume_number + '(' + self.issue_number + ').').strip()
        
        return bibliography

def citeBook():
    bibliography = Book()
    
    # A list of questions the user will be prompted with
    questions = ['Enter the author\'s first name:', 'Enter the author\'s last name:', 'Enter the year published:', 'Enter the title of the book:', 'Enter the name of the publisher:']

    bibInfo = bibliography.getInfo(questions)
    
    # Store all of the bibliography information for the Book
    bibliography.firstname = bibInfo[0]
    bibliography.lastname = bibInfo[1]
    bibliography.year_published = bibInfo[2]
    bibliography.book_title = bibInfo[3]
    bibliography.publisher = bibInfo[4]
    
    return bibliography.formatBibliography()

def citeArticle():
    bibliography = Article()
    
    # A list of questions the user will be prompted with
    questions = ['Enter the author\'s first name:', 'Enter the author\'s last name:', 'Enter the year published:', 'Enter the title of the article:', 'Enter the journal name:', 'Enter the volume number:', 'Enter the issue number:']
    
    bibInfo = bibliography.getInfo(questions)
    
    # Store all of the bibliography information for the Article
    bibliography.firstname = bibInfo[0]
    bibliography.lastname = bibInfo[1]
    bibliography.year_published = bibInfo[2]
    bibliography.article_title = bibInfo[3]
    bibliography.journal = bibInfo[4]
    bibliography.volume_number = bibInfo[5]
    bibliography.issue_number = bibInfo[6]

    return bibliography.formatBibliography()

# Loop asks the user if they want to save their bibliography
def saveBibliography(bib):
    
    # Loops until a user enters Y or N
    while(True):
        save = input('Would you like to save this bibliography? Y or N\n> ')
        
        # If Y is entered add bibliography to a list, write the list to a file, and end the loop
        # If N is entered end the loop
        if (save.upper() == 'Y' or save.upper() == 'N'):
            if (save.upper() == 'Y'):
                bibliographies.append(bib)          # Adds the bibliography to a list

                # Saves each bibliography to a file
                with open('bibliographies.txt', 'w') as f:
                    for b in bibliographies:
                        f.write("%s\n" % b)
                
                print('\nSaved to file: bibliographies.txt')
            break

def displayMenu():
    print("\nEnter the type of source you want to cite:")
    print("B: Book")
    print("A: Article")
    print("Q: Exit the program")

def main():
    print("\n  APA (7th Edition) Citation Machine\n")
    print('----------------------------------------')
    
    # Loops until the user quits
    while True:
        displayMenu()
        
        userInput = input('> ')
        if (userInput.upper() == 'Q'):
            break
        elif (userInput.upper() == 'B'):
            bib = citeBook()
            print('\nPreview of the bibliography...\n' + bib + '\n')
            saveBibliography(bib)
        elif (userInput.upper() == 'A'):
            bib = citeArticle()
            print('\nPreview of the bibliography...\n' + bib + '\n')
            saveBibliography(bib)

main()

# unit test
def test():

    print("\nStarting unit tests...")

    #TEST 1: if the user enters an invalid year, set year to 'n.d.'
    question = 'Enter the year published:'
    responses = ['two-thousand-twelve', '2022', '-10', '0']
    bibInfo = list()
    
    for response in responses :
        
        if 'year' in question:
            todays_date = date.today()
            this_year = todays_date.year
            
            # If the year is a digit and the year is between 1-2021, add it to bibInfo
            if(response.isdigit() and int(response) in range(1, this_year+1)):         
                bibInfo.append(response)
            else:                                   # else, add n.d. to bibInfo
                bibInfo.append('n.d.')

    # Each citation should be n.d.
    if all(b == 'n.d.' for b in bibInfo):
        print('TEST 1: Passed')
    else:
        print('TEST1: Failed')

# test()