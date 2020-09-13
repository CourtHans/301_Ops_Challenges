# Script:                       Op Challenge 06
# Author:                       Courtney Hans
# Date of latest revision:      9/07/20
# Purpose:                      Bash in Python

# Special thanks to a tip from Jin Kim to look up os.popen when I couldn't figure out why the output- though correct - looked funny
# resource: https://stackabuse.com/pythons-os-and-subprocess-popen-commands/

import os

# Declare variables

var_user = os.popen("whoami")
var_ip = os.popen("ip a")
var_hardware = os.popen("lshw -short")

# Declare functions

# Main

print("User information:")
print (var_user.read())

print("IP address:")
print(var_ip.read())

print("Hardware information:")
print(var_hardware.read())

# End