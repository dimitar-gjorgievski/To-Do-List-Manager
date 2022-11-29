#Imports
import util

######################
# Program Name : read
# Date Revised : November 28, 2022
# Description  : This program allows the display of the 
#                full task list, or only high priority tasks.
# 
# Functions:
#   read
#   read_high_prio
#
#######################

#Global Variables
complete, incomplete = u'\u2713', u'\u25CB'

#######################
# Function name: read
# Date Revised : November 14, 2022
# Description  : Displays the entire task list
#                including status legend and task headers.
#######################
def read(workbook):
    
    #Variables
    worksheet = workbook.active
    space_string = ""

    #Clear screen
    util.cls()

    #Display status legend
    print("    Status Legend:\n" + 
            "    " + complete + " -  Completed\n" +
            "    " + incomplete + " -  Not Completed\n")
    print("    ", end = "")

    #FOR Every row in the list
    for i, row in enumerate(worksheet.iter_rows()):

        #IF not header row
        if i > 0:

            #Get row index
            index = row[0].row - 1

            #Adjust and print row index
            if (index < 10): 
                print(" " + str(index) + ". ", end="")
            else:
                print(str(index) + ". ", end="")

        #FOR Every cell in the row
        for cell in row:

            #Adjust empty space
            space = 20 - len(str(cell.value))
            for i in range(space):
                space_string += " "

            #Print task attribute
            print (cell.value, end = space_string)
            space_string = ""

        #Print line
        print("")

        #IF header row, print line
        if i == 0:
            print("\n")

    #Print empty line
    print("\n")
        
#######################
# Function name: read_high_prio
# Date Revised : November 14, 2022
# Description  : Displays high priority tasks
#                including status legend and task headers.
#######################
def read_high_prio(workbook):

    #Local Variables
    worksheet = workbook.active
    space_string = ""
    header = ""

    #Clear Screen
    util.cls()

    #Display status legend
    print("    Status Legend:\n" + 
    "    " + complete + " -  Completed\n" +
    "    " + incomplete + " -  Not Completed\n")
    print("    ", end = "")

    #Adjust header row
    for row in worksheet[1]:
        header += row.value
        if(len(str(row.value)) < 8):
            space = 8 - len(str(row.value))
            for i in range(space):
                header += " "
        header += "            "

    #Print header
    print(header + "\n")

    #FOR Every row in the list
    for row in worksheet.iter_rows():

        #IF Task priority is High
        if row[1].value == 'High':

            #Adjust and print row index
            index = row[0].row - 1
            if (index < 10): 
                print(" " + str(index) + ". ", end="")
            else:
                print(str(index) + ". ", end="")

            #FOR Every cell in the row
            for cell in row:

                #Adjust empty space
                space = 20 - len(str(cell.value))
                for i in range(space):
                    space_string += " "

                #Print task attribute
                print (cell.value, end = space_string)
                space_string = ""
            
            #Print line
            print("")
    
    #Print empty line
    print("\n")

