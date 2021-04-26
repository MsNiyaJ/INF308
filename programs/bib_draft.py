# The following program is a tool for handling bibliographies in APA (7th Edition).

# Basic format for books in APA:
# Author, A. A. (Year of publication). Title of work: Capital letter also for subtitle. Publisher Name.

# Basic format for articles in APA:
# Author, A. A. (Year). Title of article. Name of journal, volume number(issue number)

class Book:

    # Initializes the values needed in APA (7th Edition) 
    def __init__(self):
        self.firstname = ''
        self.lastname = ''
        self.book_title = ''
        self.year_published = ''
        self.publisher = ''
        # print('Created a book')

    # Gets the information about the book
    def getInfo(self):
        self.firstname = input('\nEnter the author\'s first name.\n> ')
        self.lastname = input('\nEnter the author\'s last name.\n> ')
        self.year_published = input('\nEnter the year published.\n> ')
        
        try:
            year_published = int(self.year_published)      # Check if the user entered a valid year        
        except:
            self.year_published = 'n.d.'                   # If an invalid year was entered, set year_published to n.d.
            print("Invalid year entered...setting year to n.d.")

        # Loops until a user enters a book title
        while True: 
            self.book_title = input('\nEnter the title of the book.\n> ')
            if(self.book_title == ''):
                print("The title of the book can not be empty.")
            else:
                break
        
        self.publisher = input('\nEnter the name of the publisher.\n> ')
        
    # Formats the bibliography of the book and returns it.
    # Strips trailing and leading whitespace and capitalizes the first letter of each word
    def formatBibliography(self):

        bibliography = 'The bibliography could not be created'

        # IF the first name and last name are empty the bib starts with the title of the book
        if (self.firstname  == '' and self.lastname == ''):
            bibliography = (self.book_title.title() + ". (" + self.year_published + "). " + self.publisher).strip()
            # print(bibliography)
        
        # IF the first name and last name aren't empty create a bib
        if (self.firstname and self.lastname) != '':
            name = self.lastname + ", " + self.firstname[0] + "."        # name = lastname, first initial
            bibliography = (name.title() + " (" + self.year_published + "). " + self.book_title.title() + ". " + self.publisher).strip()
            # print(bibliography)

        # IF the first name exists and last name is empty create a bib 
        if (self.firstname != '') and (self.lastname == ''):
            name = self.firstname            # name = firstname
            bibliography = (name.title() + ". (" + self.year_published + "). " + self.book_title.title() + ". " + self.publisher).strip()
            # print(bibliography)

        # IF the first name is empty and the last name exists create a bib 
        if (self.firstname == '') and (self.lastname != ''):
            name = self.lastname            # name = lastname
            bibliography = (name.title() + ". (" + self.year_published + "). " + self.book_title.title() + ". " + self.publisher).strip()
            # print(bibliography)

        return bibliography

# Article inherits Book class
class Article(Book):
    
    def __init__(self):
        super().__init__()          # Inheriting __init__ from Book class
        self.journal = ''
        self.volume_number = ''
        self.issue_number = ''

    # Gets the information about the book
    def getInfo(self):
        self.firstname = input('\nEnter the author\'s first name:\n> ')
        self.lastname = input('\nEnter the author\'s last name:\n> ')
        self.year_published = input('\nEnter the year published:\n> ')
        
        try:
            year_published = int(self.year_published)      # Check if the user entered a valid year        
        except:
            self.year_published = 'n.d.'                   # If an invalid year was entered, set year_published to n.d.
            print("Invalid year entered...setting year to n.d.")

        # Loops until a user enters a book title
        while True: 
            self.book_title = input('\nEnter the title of the article:\n> ')
            if(self.book_title == ''):
                print("The title of the article can not be empty.")
            else:
                break
        
        self.journal = input('\nEnter the journal name:\n> ')
        self.volume_number = input('\nEnter the volume number:\n> ')
        self.issue_number = input('\nEnter the issue number:\n> ')

def citeBook():
    bibliography = Book()
    bibliography.getInfo()
    return bibliography.formatBibliography()
    
    # print('Title: ' + bibliography.book_title)
    # print('Name: ' + bibliography.firstname + ' ' + bibliography.lastname)
    # print('Year Publshed: ' + bibliography.year_published)
    # print('Publisher: ' + bibliography.publisher)

def citeArticle():
    bibliography = Article()
    bibliography.getInfo()
    

def displayMenu():
    print("\nEnter the type of source you want to cite:")
    print("B: Book")
    print("A: Article")
    print("Q: Exit the program")

def main():
    print("\n  APA (7th Edition) Citation Machine\n")
    print('----------------------------------------')
    
    bibliographies = list()     # A list of strings that will be saved to a file

    # Loops until the user quits
    while True:
        # print(bibliographies)     # Checking if the bibs are being saved properly

        displayMenu()
        
        userInput = input('> ')
        if (userInput.upper() == 'Q'):
            exit()
        elif (userInput.upper() == 'B'):
            bib = citeBook()
            print('\nPreview of the bibliography...\n' + bib + '\n')
            
            while(True):
                save = input('Would you like to save this bibliography? Y or N\n> ')
                if (save.upper() == 'Y' or save.upper() == 'N'):
                    if (save.upper() == 'Y'):
                        bibliographies.append(bib)
                    break
        elif (userInput.upper() == 'A'):
            citeArticle()

main()