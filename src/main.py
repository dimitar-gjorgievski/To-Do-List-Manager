#Imports
from src.arguments import arg_func
from src.color import pr_red

#######################
# Function name: main
# Date Revised : November 21, 2022
# Description  : Function that allows the user
#                to add items to a task list through
#                the command line or menu system.
#######################
def main():

    #TRY
    try:

        #Call arguments function
        arg_func()

    #EXCEPT File doesn't exist
    except FileNotFoundError:

        #Display no file message
        pr_red("ERROR: You do not have a Notes file.")

#Call main function
if __name__ == "__main__":
    main()
