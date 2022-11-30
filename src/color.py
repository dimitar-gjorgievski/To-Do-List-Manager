######################
# Program name : color
# Date Revised : November 11, 2022
# Description  : This program introductes color formats for outputs
#                in the project.
####################### 

#Add red color to output text 
def pr_red(skk): 

    #Add format to user red color
    print("\033[91m {}\033[00m" .format(skk))

#Add green color to output text 
def pr_green(skk): 

    #Add format to user green color
    print("\033[92m {}\033[00m" .format(skk))

#Add purple color to output text 
def pr_purple(skk): 

    #Add format to user purple color
    print("\033[95m {}\033[00m" .format(skk))

#Add cyan color to output text b
def pr_cyan(skk): 

    #Add format to user cyan color
    print("\033[96m {}\033[00m" .format(skk))
