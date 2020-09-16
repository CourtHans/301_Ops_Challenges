# Script:                       Op Challenge 13
# Author:                       Courtney Hans
# Date of latest revision:      9/16/20
# Purpose:                      Python requests library

#import library
import requests

# Declaration of variables

# asking user for simple web address
address = input("Type in a destination url (format: google.com):\n")

# concatenation with user input
user_url = str('https://' + address)

# asking user method selection and then running though logic to store in a variable
choice = input("Select an HTTP method from the following list:\n get \n post \n put \n delete \n head \n patch \n options\n")

if choice == 'get':
    method = requests.get
elif choice == 'post':
    method = requests.post
elif choice == 'put':
    method = requests.put
elif choice == 'delete':
    method = requests.delete
elif choice == 'head':
    method = requests.head
elif choice == 'patch':
    method = requests.patch
elif choice == 'options':
    method = requests.options
else:
    print("Invalid selection; we'll go with 'get'")
    method = requests.get

response = method(user_url)

# Declaration of functions

#funtion output is dependant upon user input
def run_command():
    confirm = input("Thank you for your input, please confirm you wish run the following command:\n \n requests." + choice + "('" + user_url + "') ---->  enter 'y' to confirm or 'n' to cancel  ").lower()
    
    if confirm == 'y':
        

        print("\nThe status code is:",response.status_code)
        if response.status_code == 200:
            print('That\'s the code for a successful request!')
        elif response.status_code == 307:
            print('That\'s the code for a temporary redirect')
        elif response.status_code == 400:
            print('That\'s the code for a bad request')
        elif response.status_code == 403:
            print('403? OOOH - you don\'t have access rights to that content')
        elif response.status_code == 404:
            print('That means the server can not find the requested resource')
        elif response.status_code == 405:
            print('That code means the method you selected is not allowed!')
        elif response.status_code == 408:
            print('408 means your request timed out. Your server may like to shut down this connection.')
        elif response.status_code == 429:
            print('429 means this user has sent too many requests')
        elif response.status_code == 451:
            print('451 indicates the request is unavailable for legal reasons')
  # exiting the function if anything other than y or Y is entered
    else:
        print("\nOkay, then. Re-run the script if you want to try again.")
        return None
    print('\nAnd now... your header information:\n')
    print(response.headers)


# Main

run_command()


# End