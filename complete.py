#Imports
import color, util
from read import read

#######################
# Function name: mark_complete
# Date Revised : November 28, 2022
# Description  : Allows the user to mark an existing
#                task as completed in the to-do list.
#######################
def mark_complete(workbook):

    #Local Variables
    complete, incomplete = u'\u2713', u'\u25CB'
    status_col = "C"
    worksheet = workbook.active
    todo_dir = util.get_dir_path()
    maxRow = worksheet.max_row

    #Display task list and select task to complete
    read(workbook) 
    color.pr_green("\nWhich To-Do List Item would you like mark as complete?")
    selection = input("Your Input: ")

    #IF selection is valid
    if selection != '' and int(selection) < maxRow and int(selection) > 0:

        selection = int(selection) + 1

        #IF task is not completed
        util.cls()
        if worksheet[status_col + str(selection)].value == incomplete:

            #Complete task and output success message
            worksheet[status_col + str(selection)]  = complete
            workbook.save(todo_dir + 'Notes.xlsx')
            color.pr_cyan("\nItem marked as Completed.\n")

        #ELSE
        else:

            #Output task already completed
            color.pr_cyan("\nItem is already Completed.\n")
            
    #ELSE
    else:

        #Output invalid row selection
         color.pr_red("\nInvalid row selected.\n")
