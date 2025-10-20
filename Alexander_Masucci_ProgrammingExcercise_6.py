# Alexander Masucci, Assignment #6
# Phone#, Zip & SSN Validation

import re

# check if it matches the pattern of a phone number
def phone_num_validate(num,type):

    # 2 possible patterns, with/without prefix
    validnum1 = r'\d\d\d-\d\d\d-\d\d\d\d'
    validnum2 = r'\d-\d\d\d-\d\d\d-\d\d\d\d'

    if re.match(validnum1, num) or re.match(validnum2, num):
        type = 1
    return type

# ditto, for zip codes
def zip_validate(num,type):

    # 2 possible patterns, zip or zip+4
    validnum1 = r'\d\d\d\d\d'
    validnum2 = r'\d\d\d\d\d-\d\d\d\d'

    if re.match(validnum1, num) or re.match(validnum2, num):
        type = 2
    return type

# ditto, for ssn
def ssn_validate(num,type):

    # pattern of ssn
    validnum1 = r'\d\d\d-\d\d-\d\d\d\d'

    if re.match(validnum1, num):
        type = 3
    return type

def main():

    while True:

        # Set type of number to 0 (none of them)
        type = 0

        # Get user input
        print('Please enter a valid phone number, zip code,'
          ' or social security number (including dashes).')
        num = input()

        # Call each function & get type.
        type = phone_num_validate(num,type)
        type = zip_validate(num,type)
        type = ssn_validate(num,type)

        # Print type of number it is.
        if type == 1:
            print('This is a valid phone number.')
        elif type == 2:
            print('This is a valid zip code.')
        elif type == 3:
            print('This is a valid social security number.')
        else:
            print('This is not a valid phone number, zip or ssn.')

        print()

        # continue loop or not
        cont = str.lower(input('Continue? (y/n): '))
        if cont == 'y' or cont == 'yes':
            print()
        else:
            break

main()