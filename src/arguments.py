#Imports
import argparse
from src import color, util, clear, edit, read, add, complete

#Create or load workbook
workbook = util.get_workbook()

######################
# Function name : arg_func
# Date Revised : November 29, 2022
# Description  : Function that integrates individual
#                command-line argument parsers to access
#                and modify a to-do list.
####################### 
def arg_func():

    #Create argument parser
    parser = argparse.ArgumentParser(add_help = False)

    #Add arguments to parser
    parser.add_argument("-h", "--help", action="store_true")
    parser.add_argument("-add")
    parser.add_argument("-p", "--priority", default = "Low")
    parser.add_argument("-c", "--category", default = "Other")
    parser.add_argument("-d", "--date", default = "None")
    parser.add_argument("-r", "--read", action="store_true")
    parser.add_argument("-m", "--menu", action="store_true")
    parser.add_argument("-cl", "--clear", action="store_true")
    parser.add_argument("-cla", "--clearall", action="store_true")
    parser.add_argument("-e", "--edit", action="store_true")

    #Create arguments variable
    args = parser.parse_args()

    #IF help arg is entered
    if args.help:

        #Display help message
        print ("Usage: todo.py [-add <message>] [-p | --priority <priority>]\n \
              [-c | --category <category>] [-d | --date <due date>]\n \
              Standalone arguments:\n \
              [-r | --read] [-m | --menu] [-cl | --clear] [-cla | --clearall]\n \
              [-e | --edit]\n")
        print ("\t add    \tAdd an item to the list\n \
        read    \tDisplay current to-do list\n \
        menu    \tEnter interactive menu\n \
        clear   \tDelete an individual task from list\n \
        clearall    \tDelete the entire list\n \
        edit    \tEdit an indivudal task's attribute")

    #IF add arg is entered
    if args.add:

        #Call function to add item to task list
        add.arg_add_item(args.add, args.priority, args.category, args.date, workbook)

    #IF read arg is enetered, call func to display list
    if args.read: read.read(workbook)

    #IF clear arg is entered, call func to clear item
    if args.clear: clear.clear(workbook)

    #IF clear all arg entered, call func to clear list
    if args.clearall: clear.clear_all(workbook)

    #IF edit arg is entered, call func to edit item
    if args.edit: edit.edit(workbook)
    
    #IF menu arg is entered
    if args.menu:

        #Display selection menu
        util.cls()
        color.pr_green("Choose a number from the menu options:")
        color.pr_purple(" 1. Add an Item. \n " +
        " 2. Mark Completed Item/s. \n " + 
        " 3. Delete Item/s. \n " +
        " 4. Edit Item. \n " + 
        " 5. Display All Items. \n " +
        " 6. Display High Priority Items. \n " +
        "-1. Quit.")

        #Input selection
        choice = input("\n" + " Your Input: ")

        #WHILE selection is not quit
        while (choice != '-1'):
            
            #IF add item is selected, call add func
            if choice == '1': add.menu_add_item(workbook) 

            #ELIF item completion is selected, call completion func
            elif choice == '2': complete.mark_complete(workbook)

            #ELIF item deletion is selected
            elif choice == '3':

                #Input deletion type
                util.cls()
                color.pr_green("What would you like to delete?")
                color.pr_purple(" 1. A singular item.\n" + "  2. The entire list.\n" + " -1. Quit.\n")
                deleteType = input("  Your Input: ")

                #IF delete one item is selected
                if(deleteType == '1'):

                    #Call function to delete single task item
                    clear.clear(workbook)
                
                #ELIF delete list is selected
                elif(deleteType == '2'):

                    #Call function to clear to-do list
                    clear.clear_all(workbook)

                #ELSE
                else:

                    #Display cancel message
                    color.pr_red("\nDeletion Cancelled.\n")
 
            #ELIF edit item is selected, call edit func
            elif choice == '4': edit.edit(workbook)               
            
            #ELIF read is selected, call display func
            elif choice == '5': read.read(workbook)

            #ELIF read high prio selected, call high prio func
            elif choice == '6': read.read_high_prio(workbook) 

            #ELSE 
            else:

                #Display invalid input message
                color.pr_red("ERROR: Invalid Input.\n")
            
            #Display selection menu
            color.pr_green("Choose a number from the menu options:")
            color.pr_purple(" 1. Add an Item. \n " +
            " 2. Mark Completed Item/s. \n " + 
            " 3. Delete Item/s. \n " +
            " 4. Edit Item. \n " + 
            " 5. Display All Items. \n " +
            " 6. Display High Priority Items. \n " +
            "-1. Quit.")
            
            #Input selection
            choice = input(" Your Input: ")

