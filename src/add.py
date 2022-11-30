#Imports
from datetime import date, datetime
from src import color, util

######################
# Program Name : add
# Date Revised : November 29, 2022
# Description  : This program allows the user to add tasks to a to-do
#                list either throguh command line arguments or a menu.
# 
# Functions:
#   arg_add_item
#   menu_add_item
#
#######################

#Global Variables
today = date.today()
todo_dir = util.get_dir_path()
categories = util.get_categories()
date_col = "A"
priority_col = "B"
status_col = "C"
category_col  = "D"
description_col = "E"
complete, incomplete = u'\u2713', u'\u25CB'

#######################
# Function name: arg_add_item
# Date Revised : November 24, 2022
# Description  : Allows the user to add a to-do item
#                to a list using command line arguments.
#######################
def arg_add_item(list_desc, list_prio, list_categ, list_date, workbook):

    #Local Variables
    worksheet = workbook.active
    curr_row = worksheet.max_row + 1
    description = list_desc
    priority = list_prio
    date = list_date
    status = incomplete
    category = list_categ

    #IF priority was entered
    if priority != "None":

        #Format word capitalization
        first_letter = priority[0].upper()
        rest_word = priority[1:].lower()

        #Assign priority capitalization
        priority = first_letter + rest_word
        
        #If invalid priority was entered
        if priority not in ("Low", "Medium", "High"):

            #While entered priority index is invalid
            while priority not in ("1", "2", "3"):

                #Display priority list
                color.pr_red("\nERROR: Input Must Be Low, Medium, or High.\n")
                color.pr_green("Input priority level:")
                color.pr_purple("1. Low  \n 2. Medium  \n 3. High")

                #Input priority index
                priority = input(" Your Input: ")

            #Set index to appropriate priority
            if(priority == '1'):
                priority = "Low"
            elif(priority == '2'):
                priority = "Medium"
            elif(priority == '3'):
                priority = "High"

    #IF date was entered
    if date != "None":

        #WHILE (Entered date is invalid)
        while date != '-1' and not util.check_date(date):

            #Input due date
            color.pr_red("\nERROR: Date Entered Is Invalid\n")
            color.pr_green("Input a due date (MM/DD/YYYY) or '-1' to skip.")
            date = input(" Your Input: ")

        #IF Due date exists
        if date != '-1':

            #Convert due date string to date variable
            date = datetime.strptime(date, "%m/%d/%Y").date()

            #Assign date format
            date = date.strftime("%Y-%m-%d")

        #ELSE Set date to none
        else: date = "None"

    #IF a category is selected
    if category != "None":

        #Format category variable
        firstLetter = category[0].upper()
        restWord = category[1:].lower()
        category = firstLetter + restWord
        
        #IF (Entered category is invalid)
        if not category in categories:

            #Prompt to pick a category
            color.pr_red("\nInvalid Category Entered.\n")
            util.display_categories()
            categoryIndex = input(" Your Input: ")

            #WHILE (Invalid category is selected)
            while not categoryIndex.isnumeric() or int(categoryIndex) < 1 or int(categoryIndex) > 7:
                
                #Prompt to pick a category
                color.pr_red("\nInvalid Category Selected.\n")
                util.display_categories()
                categoryIndex = input(" Your Input: ")

            #Assign input index to category variable
            category = categories[int(categoryIndex) - 1 ]

    #Write the task to excel spreadsheet
    worksheet[description_col + str(curr_row)] = description
    worksheet[priority_col + str(curr_row)] = priority
    worksheet[status_col + str(curr_row)] = status
    worksheet[category_col + str(curr_row)] = category
    worksheet[date_col + str(curr_row)] = date

    #Save the excel document
    workbook.save(todo_dir + 'Notes.xlsx')

    #Output successfully added task 
    print (f"\n Item    : {description} \n Priority: {priority} \
             \n Category: {category} \n Due Date: {date}")
    color.pr_cyan("Added Successfully.\n")

######################
# Function Name: menu_add_item
# Date Revised : November 29, 2022
# Description  : This functions allows the user to add items
#                to a to-do list through a menu selection interface.
####################### 
def menu_add_item(workbook):

    #Local Variables
    worksheet = workbook.active
    curr_row = worksheet.max_row + 1
    status = incomplete

    #Input task description
    util.cls()    
    color.pr_green("Input the description of the To-Do List item.")
    description = input(" Your Input: ")

    #Input priority level
    util.cls()
    color.pr_green("Input priority level:")
    color.pr_purple("1. Low  \n 2. Medium  \n 3. High")
    priority = input(" Your Input: ")

    #WHILE Invalid priority is entered
    while priority not in ("1", "2", "3"):

        #Input priority level
        color.pr_red("\nERROR: Input Must Be High, Meduim, or Low.\n")
        color.pr_green("Input priority level:")
        color.pr_purple("1. Low  \n 2. Medium  \n 3. High")
        priority = input(" Your Input: ")

    #Set index to appropriate priority
    if priority == '1':
        priority = "Low"
    elif priority == '2':
        priority = "Medium"
    elif priority == '3':
        priority = "High"

    #Select category
    util.cls()
    util.display_categories()
    categoryIndex = input(" Your Input: ")

    #WHILE Invalid category is selected
    while not categoryIndex.isnumeric() or int(categoryIndex) < 1 or int(categoryIndex) > 7:
        
        #Select category
        color.pr_red("\nInvalid Category Selected.\n")
        util.display_categories()
        categoryIndex = input(" Your Input: ")

    #Assign input index to category variable
    category = categories[int(categoryIndex) - 1 ]

    #Input due date
    util.cls()
    color.pr_green("Input a due date (MM/DD/YYYY) or '-1' to skip.")
    date = input(" Your Input: ")

    #WHILE Entered date is invalid
    while date != '-1' and not util.check_date(date):

        #Input due date
        color.pr_red("\nERROR: Date Entered Is Invalid\n")
        color.pr_green("Input a due date (MM/DD/YYYY) or '-1' to skip.")
        date = input(" Your Input: ")

    #IF Task has no due date, set to None
    if date == '-1': date = "None"

    #ELSE
    else:
        
        #Convert due date string to date variable
        date = datetime.strptime(date, "%m/%d/%Y").date()

        #Assign date format
        date = date.strftime("%Y-%m-%d")

    #Write task to excel spreadsheet
    worksheet[description_col + str(curr_row)] = description
    worksheet[priority_col + str(curr_row)] = priority
    worksheet[status_col + str(curr_row)] = status
    worksheet[category_col + str(curr_row)] = category
    worksheet[date_col + str(curr_row)] = date

    #Save the excel document
    workbook.save(todo_dir + 'Notes.xlsx')

    #Output successfully added task
    print (f"\n Item    : {description} \n Priority: {priority} \
             \n Category: {category} \n Due Date: {date}")
    color.pr_cyan("Added Successfully.\n")