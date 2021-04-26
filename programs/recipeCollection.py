# The following program is a tool for saving and accessing recipes.

recipes = dict()        # A dictionary that will hold all recipes

file = None             # global variable that is used when a user saves a file

def addANewRecipe():
    
    new_recipe = dict()     # Creating a dictionary to hold new recipe info
    
    recipe_name = input("\nEnter a recipe name...\n> ")
    
    # Prints the recipe if it already exists
    if recipe_name in recipes:
        print("Error: This recipe already exists")
        print(recipes[recipe_name]) 
    else:
        new_recipe['name'] = recipe_name       #Adds the recipe name to the dictionary
        
        ingredients = input("\nEnter the ingredients for this recipe...\n> ")
        new_recipe['ingredients'] = ingredients     #Adds the ingredients to the dictionary
        
        instructions = input("\nEnter the instructions for this recipe...\n> ")
        new_recipe['instructions'] = instructions     #Adds the instructions to the dictionary    
        
        recipes[recipe_name] = new_recipe             #Adds a new recipe to the list of recipes

def listExistingRecipes():
    print("\nListing all of your recipes...")
        
    # Prints out every recipe in recipes
    for key in recipes:
        print(key)

    # Displays a message if no recipes were found
    recipesExist = bool(recipes)
    if(recipesExist is False):
        print("No recipes were found.")

    input('\nPress enter to continue...')

def readRecipes():

    recipe = input("\nWhich recipe would you like to see?\n> ")
    
    # Displays the recipe the user is looking for, displays message if it doesn't exist
    if recipe not in recipes:
        print("Error: This recipe does not exist. Try adding the recipe.") 
    else:
        print("\nDisplaying your recipe...")
        
        rec = recipes[recipe]       # The dictionary of the recipe the user is looking for 
        
        # print the recipe details
        for r in recipes[recipe]:
            print(r + ': ' + rec[r])

    input('\nPress enter to continue...')

def saveRecipes():
    print("Saving your recipes...")
    
    # Creates a file called recipes
    file = open('recipes.tsv', 'w')
   
    # Add a heading to the text file
    headings = "Name\t\t\t\t\t\tIngredients\t\t\t\t\t\tInstructions\n"
    file.write(headings)

    # Save each recipe to a file
    for key in recipes:
    
        recipe_name = recipes[key]["name"]
        ingredients = recipes[key]["ingredients"]
        instructions = recipes[key]["instructions"]

        recipe = recipe_name+"\t\t\t\t\t\t"+ingredients+"\t\t\t\t\t\t"+instructions+"\n"
        file.write(recipe)

def displayMenu():
    print("\nChoose one of the following options:")
    print("N: Add New Recipe")
    print("L: List Existing Recipes")
    print("R: Read Recipe")
    print("S: Save Recipes")
    print("Q: Quit")

def main():
    # Allows a user to do options from the menu until they quit the program
    while True:
        displayMenu()

        # Changes the input to uppercase letters
        option = input("\n> ").upper()
        
        # Ends the program if a user enters 'Q'    
        if option == "Q":

            # Closes the file if the user quits the program
            if(file is not None): 
                file.close()
            break

        # Calls a function based on the users input
        if(option == "N"):
            addANewRecipe()
        elif(option == "L"):
            listExistingRecipes()
        elif(option == "R"):
            readRecipes()
        elif(option == "S"):
            saveRecipes()

main()