# Script:                       Op Challenge 11
# Author:                       Courtney Hans
# Date of latest revision:      9/14/20
# Purpose:                      File Handling in Python

import os

# Declaration of variables

# Declaration of functions

# Main
# creating the file & putting some starter content in it
file0 = open("myNewFile.txt", "w")
file0.write("Here's my file for Challenge #11")
file0.close()

# initial reading
file1 = open("myNewFile.txt", "r")
print("INITIAL contents of my file:")
print()
print(file1.read())
file1.close()

# appending 3 lines
fileA = open("myNewFile.txt", "a")
fileA.write("\n")
fileA.write("Now I have more lines (this is new line #1) \n")
fileA.write("New line #2 \n")
fileA.write("New line #3")
fileA.close()

print()
# read after appending
print("HERE are the contents after adding 3 new lines:")
fileB = open("myNewFile.txt", "r")
print()
print(fileB.read())
fileB.close()

print()
# show just the first line)
print("NOW I'm showing you just the first line:")
print()
file2 = open("myNewFile.txt", "r")
print(file2.readline())
file2.close()

# delete the file
os.remove("myNewFile.txt")
print("I have now deleted the file.")

# End