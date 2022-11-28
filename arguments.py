#Imports
import argparse
import color
import util
import clear, edit, read, add, complete

#Create or load workbook
workbook = util.get_workbook()

######################
# Program name : arg_func
# Date Revised : November 25, 2022
# Description  : Function that integrates individual
#                command-line argument parsers to access
#                and modify a to-do list.
####################### 
def arg_func():

    #Configure message
    msg= "A command-line utility tool that allows the user to configure a To-Do list of items."

    #Create argument parser
    parser = argparse.ArgumentParser(description = msg)

    #Add arguments to parser
    parser.add_argument("-help", "--Help", help = "Help menu", action="store_true")
    parser.add_argument("-add", "--Add", help = "Add item to list.")
    parser.add_argument("-p", "--Priority", help = "")
    parser.add_argument("-c", "--Category", help = "")
    parser.add_argument("-d", "--Date", default = "None", help = "")
    parser.add_argument("-r", "--Read", help = "Display the full To-Do list.", action="store_true")
    parser.add_argument("-m", "--Menu", help = "Open interactive menu with all modification features included.", action="store_true")
    parser.add_argument("-cl", "--Clear", help = "Open prompt to delete a single item in the list.", action="store_true")
    parser.add_argument("-cla", "--Clear_all", help = "Open prompt to delete the entire To-Do list", action="store_true")
    parser.add_argument("-e", "--Edit", help = "Open prompt to edit a specific item in the list. ", action="store_true")


    args = parser.parse_args()



    if args.Help:
        print ("\t todo.py -add [ItemDescription] -p [Priority](Optional) -d [DueDate](Optional) -c [Category](Optional) - add a task \n \
        todo.py -m   - Open interactive menu  \n \
        todo.py -r   - Display full list \n \
        todo.py -e   - Edit a specific task in list \n \
        todo.py -cl  - Delete single task in list \n \
        todo.py -cla - Delete entire to-do list")

    if args.Add:
        add.arg_add_item(args.Add, args.Priority, args.Category, args.Date, workbook)

    if args.Read:
        read.read(workbook)

    if args.Clear:
        clear.clear(workbook)

    if args.Clear_all:
        clear.clear_all(workbook)

    if args.Edit:
        edit.edit(workbook)
    
    if args.Menu:

        util.cls()

        color.pr_green("Choose a number from the menu options:")
        color.pr_purple(" 1. Add an Item. \n " +
        " 2. Mark Completed Item/s. \n " + 
        " 3. Delete Item/s. \n " +
        " 4. Edit Item. \n " + 
        " 5. Display All Items. \n " +
        " 6. Display High Priority Items. \n " +
        "-1. Quit.")

        choice = input("\n" + " Your Input: ")

        while (choice != '-1'):
            
            if choice == '1':
                add.menu_add_item(workbook) 

            elif choice == '2':
                complete.mark_complete(workbook)

            elif choice == '3':
                util.cls()
                color.pr_green("What would you like to delete?")
                color.pr_purple(" 1. A singular item.\n" + "  2. The entire list.\n" + " -1. Quit.\n")
                deleteType = input("  Your Input: ")

                if(deleteType == '1'):
                    clear.clear(workbook)
                elif(deleteType == '2'):
                    clear.clear_all(workbook)
                else:
                    color.pr_red("\nDeletion Cancelled.\n")
 
            elif choice == '4':
                edit.edit(workbook)               
            
            elif choice == '5':
                read.read(workbook)

            elif choice == '6':
                read.read_high_prio(workbook) 

            else:
                color.pr_red("ERROR: Invalid Input.\n")
            
            color.pr_green("Choose a number from the menu options:")
            color.pr_purple(" 1. Add an Item. \n " +
            " 2. Mark Completed Item/s. \n " + 
            " 3. Delete Item/s. \n " +
            " 4. Edit Item. \n " + 
            " 5. Display All Items. \n " +
            " 6. Display High Priority Items. \n " +
            "-1. Quit.")
            
            choice = input(" Your Input: ")

