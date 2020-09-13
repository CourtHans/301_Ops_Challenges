# Script:                       Op Challenge 09
# Author:                       Courtney Hans
# Date of latest revision:      9/10/20
# Purpose:                      List manipulation in Python

# Declaration of variables

court_list = ["Yosemite", "Yellowstone", "Glacier", "Grand Canyon", "Zion", "Grand Tetons", "Bryce", "Arches", "Rocky Mountain", "Haleakala"]

# Declaration of functions

# Main
print("Full list:")
print(court_list)

# print the fourth element of the list
print("4th element only:")
print(court_list[3])

# print the sixth through tenth elements of the list
print("Elements 6-10 only:")
print(court_list[5:])

# change the value of the seventh element to "onion"
print("Changing 7th element to 'onion':")
court_list[6] = "onion"
print(court_list)



# End