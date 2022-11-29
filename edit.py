#Imports
import color, util
from read import read

#Global Variables
todo_dir = util.get_dir_path()
date_col = "A"
priority_col = "B"
category_col = "D"
description_col = "E"

desc_index = '1'
prio_index = '2'
cat_index = '3'
date_index = '4'

#######################
# Function name: edit
# Date Revised : November 28, 2022
# Description  : Allows the user to edit a specific
#                tasks' description, priority, category, or due date.
#######################
def edit(workbook):

    #Local Variables
    worksheet = workbook.active
    categories = util.get_categories()
    maxRow = worksheet.max_row

    #Display to-do list
    util.cls()
    read(workbook)

    #Select task to be edited
    color.pr_green("\nWhich task item would you like to edit?")
    selection = input("Your Input: ")

    #IF valid input is selected
    if selection != '' and int(selection) < maxRow and int(selection) > 0:

        selection = int(selection) + 1

        #Select desired attribute to be edited
        util.display_row(workbook, selection)
        color.pr_green("\nWhich attribute would you like to update?")
        color.pr_purple("1. Description \n" + 
                       " 2. Priority \n" +
                       " 3. Category \n" +
                       " 4. Due Date \n")
        editType = input("Your Input: ")

        #IF Edit select is for task description
        if editType == desc_index:

            #Input new description
            util.cls()
            color.pr_green("What would you like to change the description to? (-1 to Quit)")
            newDesc = input("Your Input: ")

            #Update description
            if(newDesc != '-1'):
                worksheet[description_col + str(selection)] = newDesc
                color.pr_cyan("\nItem edited successfully.\n")
                workbook.save(todo_dir + 'Notes.xlsx')
            else:
                color.pr_red("\nItem edit cancelled.\n")

        #ELIF Edit select is for priority
        elif editType == prio_index:

            #Input new priority
            util.cls()
            color.pr_green("Input priority level:")
            color.pr_purple(" 1. Low  \n " +
                " 2. Medium  \n " +
                " 3. High \n " + 
                "-1. Quit")
            priority = input("\n" + " Your Input: ")

            #Change priority to appropriate index IF valid input entered
            if priority == "1":
                worksheet[priority_col + str(selection)] = "Low"
                color.pr_cyan("\nPriority successfully changed.\n")

            elif priority == "2":
                worksheet[priority_col + str(selection)] = "Medium"
                color.pr_cyan("\nPriority successfully changed.\n")

            elif priority == "3":
                worksheet[priority_col + str(selection)] = "High"
                color.pr_cyan("\nPriority successfully changed.\n")

            #ELSE 
            else:

                #Display invalid input message
                color.pr_red("\nInvalid priority selected. File edit cancelled.\n")

        #ELIF Edit select is for category
        elif editType == cat_index:

            #Select new category
            util.cls()
            util.display_categories()
            categoryIndex = input( " Your Input: ")

            #IF Valid category selected
            if categoryIndex != '' and int(categoryIndex) >= 1 and int(categoryIndex) <= 7:
                
                #Update task category
                category = categories[int(categoryIndex) - 1 ]    
                worksheet[category_col + str(selection)] = category
                workbook.save(todo_dir + 'Notes.xlsx')
                color.pr_cyan("\nCategory successfully changed.\n")

            #ELSE
            else:
                
                #Display invalid category input
                color.pr_red("\nInvalid category entered. File edit cancelled.\n")

        #ELIF Edit select is for due date
        elif editType == date_index:

            #Input new due date
            util.cls()
            color.pr_green("What will the new Due Date be? (MM/DD/YYYY)")
            date = input(" Your Input: ")

            #IF entered date is valid
            if util.check_date(date):

                #Update due date
                worksheet[date_col + str(selection)] = date
                workbook.save(todo_dir + 'Notes.xlsx')
                color.pr_cyan("\nDate successfully changed.\n")

            #ELSE
            else:

                #Display invalid date message
                color.pr_red("\nInvalid date entered. File edit cancelled.\n")

        #ELSE
        else:

            #Display invalid edit type
            color.pr_red("\nInvalid edit type. File edit cancelled.\n")

        #Save all changes to task list
        workbook.save(todo_dir + 'Notes.xlsx')

    #ELSE
    else:

        #Display invalid row message
        color.pr_red("\nInvalid row selected. File edit cancelled.\n")

