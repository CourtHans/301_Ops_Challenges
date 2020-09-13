# Script Name:              Ops Challenge 07
# Author:                   Courtney Hans
# Date of last revision:    9/9/20
# Description of purpose:   Functions in Python

# Import libraries

import os

# Declaration of variables

### Read user input here into a variable
user_input = input("Type in the name of a directory from the home folder:")

# Declaration of functions

### Declare a function here

def first_python_function(dir_name):
    for (root, dirs, files) in os.walk("/home/osboxes/" + dir_name):
        ### Add a print command here to print ==root==
        print("==root==")
        print(root)
        ### Add a print command here to print ==dirs==
        print("==dirs==")
        print(dirs)
        ### Add a print command here to print ==files==
        print("==files")
        print(files)

# Main

### Pass the variable into the function here

first_python_function(user_input)

# End