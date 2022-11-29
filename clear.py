#Imports
import color, util
from read import read

######################
# Program Name : clear
# Date Revised : November 28, 2022
# Description  : This program allows the user to delete
#                a single task item from the list, or to
#                delete the entire list completely.
# 
# Functions:
#   clear
#   clear_all
#
#######################

#Global Variables
todo_dir = util.get_dir_path()

#######################
# Function name: clear
# Date Revised : November 28, 2022
# Description  : Allows user to clear specific task
#                from the to-do list.
#######################
def clear(workbook):

    #Local Variables
    worksheet = workbook.active
    maxRow = worksheet.max_row

    #Clear Screen
    util.cls()

    #Display full task list
    read(workbook)

    #Input task to delete
    color.pr_green("\nSelect row item to be deleted.")
    selection = input("Your Input: ")

    #IF Valid index is entered
    if (selection != '' and int(selection) < maxRow and int(selection) > 0):

        #Local Variables
        selection = int(selection) + 1
        header = ""
        spaceString = ""

        #Clear screen
        util.cls()

        #Adjust header row
        for row in worksheet[1]:
            header += row.value
            if(len(str(row.value)) < 8):
                space = 8 - len(str(row.value))
                for i in range(space):
                    header += " "
            header += "            "

        #Display header row
        print(header + "\n")

        #FOR Every attribute of the task
        for cell in worksheet[selection]:

            #Adjust empty space
            space = 20 - len(str(cell.value))
            for i in range(space):
                spaceString += " "

            #Display attribute
            print (cell.value, end = spaceString)
            spaceString = ""
        
        #Print line
        print("")

        #Input delete confirmation
        color.pr_green("\nAre you sure you want to delete this row? (Y / N)")
        choice = input("Your Input: ")
        choice = choice.lower()

        #IF choice is yes
        if(choice == "y"):

            #Delete task
            worksheet.delete_rows(selection)

            #Save task list and display success message
            workbook.save(todo_dir + 'Notes.xlsx')
            color.pr_cyan("\nRow deleted successfully.\n")

        #ELSE
        else:

            #Display cancel message
            color.pr_red("\nCanceled row deletion.\n")

    #ELSE
    else:

        #Display invalid input message
        color.pr_red("\nInvalid row selected. Deletion canceled.\n")

#######################
# Function name: clear_all
# Date Revised : November 14, 2022
# Description  : Allows user to clear an entire
#                to-do list.
#######################
def clear_all(workbook):

    #Local Variables
    worksheet = workbook.active

    #Input deletion confirmation
    util.cls()
    color.pr_red("WARNING: Are you sure you want to clear all of your To-Do List items? (Y / N)")
    choice = input(" Your Input: ")
    choice = choice.lower()

    #IF Input is yes
    if choice == 'y':

        #Delete to-do list
        worksheet.delete_rows(2, worksheet.max_row)

        #Save changes and display success message
        workbook.save(todo_dir + 'Notes.xlsx')
        color.pr_cyan("\nTo-Do List cleared.\n")
    
    #ELSE
    else:

        #Display cancel message
        color.pr_red("\nFile deletion canceled.\n")