# Alexander Masucci, Assignment #1
# Ticket Pre-sale

# Main function
def main():
    print('Cinema Ticket Pre-Sale Simulator.')

    # Number of tickets remaining
    tickets = 20

    # Loop until no tickets remain
    while tickets > 0:
        print()
        print(f'There are {tickets} tickets remaining.')

        # Call function and set new total ticket value
        tickets = tic_input(tickets)

    print('All tickets have been purchased. Thank you for your time.')


# First function prompts user to buy tickets and subtracts it from total.
def tic_input(tickets):

    # Preamble.
    print()
    print('How many tickets would you like to purchase?')
    print('Please enter a number between 1 and 4.')

    # User input a number of tickets they want to buy.
    try:
        ticket_buy = int(input())
    except:
        print('Please input a number.')
        return tickets


    # Check if there are enough tickets remaining.
    if ticket_buy > tickets:
        print('Sorry, there are not enough tickets remaining.')
        return tickets #

    # Check if there was a valid number of tickets input.
    if ticket_buy in range(0, 5):
        # Subtract tickets bought from total tickets
        tickets -= ticket_buy
        print(f'You have purchased {ticket_buy} tickets.')
        # Return new value
        return tickets
    elif ticket_buy > 4:
        print('Please purchase only 4 tickets or less.')
        return tickets
    else:
        print('Invalid input. Please try again.')
        return tickets

main()