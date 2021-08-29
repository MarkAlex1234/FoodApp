# Food App
# Mark Alexander 2021

# This app is designed to help my girlfriend find ideas for meals.
# It grabs a random meal for breakfast,lunch or dinner.
# Also gives a link to a recipe, and gives details on the cook time for the meal.
# At the end displaying the 3 course plan for the day.

import sys
import os
import time
import random

def print_slow(str): #FUNCTION TO PRINT STRINGS SLOW
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)
def print_slower(str): #FUNCTION TO PRINT STRINGS SLOWER
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
def print_superslow(str): #FUNCTION TO PRINT STRINGS SUPERSLOW
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(1)

def startUp():
    print("")
    os.system('cls')
    print_slow("""
##################################################
#                                                #\n#              """)
    print_slower("GLUTEN-FREE FOOD IDEAS")
    print_slow("""            #\n#                                                #
################################################## 
#                    MAIN MENU                   #
#                  --- Start ---                 #       
#                  --- About ---                 #       
#                  --- Quit ---                  #
############################################""")
    print_slower("######")
    startUpOptions();

def startUpOptions():
    print("");
    option = input("\nUserInput>");
    while option.lower() not in ['start','about','quit']:
            print("Please enter a vaild command");
            option = input("\nUserInput> ");
    if option.lower() == ("start"):
        findBreakfast();
    elif option.lower() == ("about"):
        helpMenu();
    elif option.lower() == ("quit"):
        quitApp();

def helpMenu():
    os.system("cls");
    print("""
    -------------------------------
    |           ABOUT MENU        |
    -------------------------------

    --- ABOUT ---
    # This app is designed to help my girlfriend find ideas for meals.
    # It grabs a random meal for breakfast,lunch or dinner.
    # Also gives a link to a recipe, and gives the cooktime for the meal.
    # If you have already had that meal, you can simply skip.
    
    -----------------------------------------------------------------------------------
""")

    closeHelpMenu = input("\nTo close menu type 'Y':")
    closeHelpMenu = closeHelpMenu.upper()
    while closeHelpMenu != 'Y':
        print("\n>Invaild Command")
        closeHelpMenu = input("\nTo close menu type 'Y':")
        closeHelpMenu = closeHelpMenu.upper()
    if closeHelpMenu == "Y":
        startUp();

def quitApp():
    print_slow(">Exiting");
    print_superslow("...");
    sys.exit();

#############################################################################################################
#############################################################################################################
#############################################################################################################

def findBreakfast():
    os.system("cls");
    userInput = input("\n>Have you had breakfast? 'Y/N' ")
    userInput = userInput.upper()
    while userInput.upper() not in ['Y','N','QUIT']:
            print("\nPlease enter a vaild command");
            userInput = input("\n> ");
    if userInput == "QUIT":
        quitApp();
    elif userInput == "Y":
        findLunch();
    elif userInput == "N":
        randomNum = random.randint(1,10);
        breakfastMeal(randomNum);
        

def findLunch():
    userInput = input("\n>Have you had Lunch? 'Y/N' ")
    userInput = userInput.upper()
    while userInput.upper() not in ['Y','N','QUIT']:
            print("\nPlease enter a vaild command");
            userInput = input("\n> ");
    if userInput == "QUIT":
        quitApp();
    elif userInput == "Y":
        findDinner();
    elif userInput == "N":
        randomNum = random.randint(1,10);
        lunchMeal(randomNum)
            
            
def findDinner():
    userInput = input("\n>Have you had Dinner? 'Y/N' ")
    userInput = userInput.upper()
    while userInput.upper() not in ['Y','N','QUIT']:
            print("\nPlease enter a vaild command");
            userInput = input("\n> ");
    if userInput == "QUIT":
        quitApp();
    elif userInput == "Y":
        finalMessage();
        pressAnyKey();
        quitApp();
    elif userInput == "N":
        randomNum = random.randint(1,10);
        dinnerMeal(randomNum);

#############################################################################################################
#############################################################################################################
#############################################################################################################
        
def breakfastMeal(int):
        os.system("cls");
        print("""
\n               --------------------------
               |        BREAKFAST       |
               --------------------------
               """)
        if int == 1:
            displayMeal("Cloud Eggs", 20);
            print("\nRecipe: https://www.delish.com/cooking/recipe-ideas/recipes/a52748/cloud-eggs-recipe/");
            pressAnyKey()
            findLunch();
        elif int == 2:
            displayMeal("Breakfast Wraps", 15);
            print("\nRecipe: https://www.delish.com/cooking/recipe-ideas/recipes/a57866/low-carb-breakfast-wraps-recipe/");
            pressAnyKey()
            findLunch();
        elif int == 3:
            displayMeal("Bunless Bacon, Egg & Cheese", 15);
            print("\nRecipe: https://www.delish.com/cooking/recipe-ideas/recipes/a51637/bunless-bacon-egg-and-cheese-recipe/");
            pressAnyKey()
            findLunch();
        elif int == 4:
            displayMeal("Cauliflower Toast", 45);
            print("\nRecipe: https://www.delish.com/cooking/recipes/a50033/cauliflower-toast-recipe/");
            pressAnyKey()
            findLunch();
        elif int == 5:
            displayMeal("Bacon, Egg, and Cheese Roll-Ups", 20);
            print("\nRecipe: https://www.delish.com/cooking/recipe-ideas/recipes/a52582/bacon-egg-and-cheese-roll-ups-recipe/");
            pressAnyKey()
            findLunch();
        elif int == 6:
            displayMeal("Cream Cheese Pancakes", 15);
            print("\nRecipe: https://www.delish.com/cooking/recipe-ideas/recipes/a53097/cream-cheese-pancakes-recipe/");
            pressAnyKey()
            findLunch();
        elif int == 7:
            displayMeal("Paleo Breakfast Stacks", 30);
            print("\nRecipe: https://www.delish.com/cooking/recipe-ideas/recipes/a54408/paleo-breakfast-stacks-recipe/");
            pressAnyKey()
            findLunch();
        elif int == 8:
            displayMeal("Bacon Weave Breakfast Tacos", 60);
            print("\nRecipe: https://www.delish.com/cooking/recipe-ideas/recipes/a54272/bacon-weave-breakfast-tacos/");
            pressAnyKey()
            findLunch();
        elif int == 9:
            displayMeal("Avocado Toast", 5);
            print("\nRecipe: https://www.hotpankitchen.com/simple-avocado-toast/");
            pressAnyKey()
            findLunch();
        elif int == 10:
            displayMeal("Special K® Gluten Free", 2);
            print("\nRecipe: https://www.kelloggs.co.nz/en_NZ/products/special-k-gluten-free-product.html");
            pressAnyKey()
            findLunch();
            
def lunchMeal(int):
        print("""\n               ------------------------
               |        LUNCH         |
               ------------------------""")
        if int == 1:
            displayMeal("Butter Chicken", 35);
            print("\nRecipe: https://offthewheatenpathtt.com/2020/03/01/gluten-free-easy-butter-chicken/");
            pressAnyKey()
            findDinner();
        elif int == 2:
            displayMeal("Pizza", 30);
            print("\nRecipe: http://www.imglutenfree.com/easy-30-minute-gluten-free-pizza-crust-recipe/");
            pressAnyKey()
            findDinner();
        elif int == 3:
            displayMeal("Mac n Cheese", 20);
            print("\nRecipe: https://raiasrecipes.com/2015/04/easy-one-pot-mac-n-cheese-with-hidden-veggies.html");
            pressAnyKey()
            findDinner();
        elif int == 4:
           displayMeal("Butternut Squash Salmon", 40);
           print("\nRecipe: https://www.thisvivaciouslife.com/one-pan-whole30-butternut-squash-salmon/");
           pressAnyKey()
           findDinner();
        elif int == 5:
            displayMeal("Thai Red Curry ", 25);
            print("\nRecipe: https://glutenfreecuppatea.co.uk/2019/07/18/gluten-free-thai-red-curry-recipe-vegan/");
            pressAnyKey()
            findDinner();
        elif int == 6:
            displayMeal("Macho Nachos", 50);
            print("\nRecipe: https://www.thespruceeats.com/gluten-free-macho-nacho-recipe-1450868");
            pressAnyKey()
            findDinner();
        elif int == 7:
            displayMeal("Bolognaise Bake", 70);
            print("\nRecipe: https://www.taste.com.au/recipes/gluten-free-bolognaise-bake-recipe/2gj8fxzv?r=recipes/top50glutenfreedinners&c=X2Hpm9YR/Top%2050%20gluten%20free%20dinners");
            pressAnyKey()
            findDinner();
        elif int == 8:
            displayMeal("Bolognese", 35);
            print("\nRecipe: https://www.taste.com.au/recipes/bolognese-2/acdb2f40-7343-4a08-9698-4672a19c285c?r=recipes/top50glutenfreedinners&c=X2Hpm9YR/Top%2050%20gluten%20free%20dinners");
            pressAnyKey()
            findDinner();
        elif int == 9:
            displayMeal("Meatballs", 20);
            print("\nRecipe: https://www.mamaknowsglutenfree.com/gluten-free-meatballs/");
            pressAnyKey()
            findDinner();
        elif int == 10:
            displayMeal("Pear & pork salad with pecans & blue cheese", 15);
            print("\nRecipe: https://www.taste.com.au/recipes/pear-pork-salad-pecans-blue-cheese/ae0efc38-61c4-41a1-9d59-d0d756bf5fb9");
            pressAnyKey()
            findDinner();

def dinnerMeal(int):
        print("""\n               ------------------------
               |        DINNER        |
               ------------------------""")
        if int == 1:
            displayMeal("Grilled Lamb with Root Vegetables and Sumac", 45);
            print("\nRecipe: https://www.foodinaminute.co.nz/recipe/grilled-lamb-with-root-vegetables-and-sumac-546662?categoryid=1000031");
            finalMessage()
            pressAnyKey()
            quitApp();
        elif int == 2:
            displayMeal("Garlic & White Bean Purée", 15);
            print("\nRecipe: https://www.foodinaminute.co.nz/recipe/garlic-white-bean-pure-548203?categoryid=1000031")
            finalMessage()
            pressAnyKey()
            quitApp();
        elif int == 3:
            displayMeal("Lamb Korma with Saag Aloo", 30);
            print("\nRecipe: https://www.foodinaminute.co.nz/recipe/lamb-korma-with-saag-aloo-356587?categoryid=1000031")
            finalMessage()
            pressAnyKey()
            quitApp();
        elif int == 4:
            displayMeal("Honey Soy Chicken", 20)
            print("\nRecipe: https://www.mygfguide.com/gluten-free-honey-soy-chicken/");
            finalMessage()
            pressAnyKey()
            quitApp();
        elif int == 5:
            displayMeal("Sweet Chicken", 35)
            print("\nRecipe: https://mygluten-freekitchen.com/5-ingredient-sweet-chicken-gluten-free/");
            finalMessage()
            pressAnyKey()
            quitApp();
        elif int == 6:
            displayMeal("Chicken Bacon Ranch Casserole", 30)
            print("\nRecipe: https://glutenfreeonashoestring.com/gluten-free-chicken-bacon-ranch-casserole/");
            finalMessage()
            pressAnyKey()
            quitApp();
        elif int == 7:
            displayMeal("Baked Salmon", 20)
            print("\nRecipe: https://downshiftology.com/recipes/best-baked-salmon/");
            finalMessage()
            pressAnyKey()
            quitApp();
        elif int == 8:
            displayMeal("Moo Goo Gai", 30)
            print("\nRecipe: https://allergyawesomeness.com/30-minute-moo-goo-gai-pan-gluten-dairy-egg-peanut-and-tree-nut-free/");
            finalMessage()
            pressAnyKey()
            quitApp();
        elif int == 9:
            displayMeal("Taco Salad", 10)
            print("\nRecipe: https://www.wholesomeyum.com/recipes/taco-salad/");
            finalMessage()
            pressAnyKey()
            quitApp();
        elif int == 10:
            displayMeal("Korean BBQ Salmon Stir Fry", 10)
            print("\nRecipe: https://strengthandsunshine.com/korean-bbq-salmon-stir-fry/");
            finalMessage();
            pressAnyKey()
            quitApp();
            
#############################################################################################################
#############################################################################################################
#############################################################################################################

def pressAnyKey():
    userInput = input("\n\n(Press 'ANY-KEY' to continue)");

def displayMeal(str, int):
    title = str; 
    cookTime = int;
    print("""\n------------------------------------------------------
For this meal we are having: %s

This meal has a cook time of: %d minutes!
------------------------------------------------------"""%(title,cookTime));

def finalMessage():
 print("""\n
################################################################
#    Save this meal plan then press any key to quit!           #
################################################################""")

#############################################################################################################
#############################################################################################################
#############################################################################################################


                                                ### Functions ###
startUp();
#startUpOptions();
#helpMenu();
#findBreakfast();
#findLunch();
#findDinner();
#breakfastMeal();
#lunchMeal();
#dinnerMeal();
#displayMeal();
#quitApp();


