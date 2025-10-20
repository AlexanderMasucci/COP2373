# Alexander Masucci, Assignment #3
# Monthly Expense List

import functools

def main():

    # Initialize a list for expense input
    expense_list = []

    # Get expenses from user
    loopbool = True
    while loopbool != False:
        expense_type = input('What type of expense is it? ')
        try:
            expense_amount = float(input('How much is this expense? $'))
            expense_list.append((expense_type, expense_amount))
            print()
        except ValueError:
            print('Please enter a number.')
        yn = input('Continue? (y/n): ')
        yn = yn.lower()
        if yn == 'n' or yn == 'no':
            loopbool = False

    expense_total = functools.reduce(lambda x, y: x + y, expense_list)
    print(expense_total)
    expense_high = 'h'
    expense_low = 'x'

main()