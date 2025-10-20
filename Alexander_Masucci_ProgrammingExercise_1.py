# Alexander Masucci, Assignment #1
# Ticket Pre-sale

# Main function
def main():
    print('Cinema Ticket Pre-Sale Simulator.')

    # Number of tickets remaining
    tic_total = 10

    # Loop until no tickets remain
    while tic_total > 0:
        print()
        print(f'There are {tic_total} tickets remaining.')

        # Call function and set new total ticket value
        tic_total = tic_input(tic_total)

    print('All tickets have been purchased. Thank you for your time.')


# First function prompts user to buy tickets and subtracts it from total.
def tic_input(tic_total):

    # Preamble.
    print()
    print('Please choose a number of tickets to be purchased, from 1 to 4.')

    # User input a number of tickets they want to buy.
    try:
        ticket_buy = int(input())
    except:
        print('Please input a number.')
        return tic_total


    # Check if there are enough tickets remaining.
    if ticket_buy > tic_total:
        print('Sorry, there are not enough tickets remaining.')
        return tic_total

    # Check if there was a valid number of tickets input.
    if ticket_buy in range(0, 5):
        # Subtract tickets bought from total tickets
        tic_total -= ticket_buy
        print(f'You have purchased {ticket_buy} tickets.')
        # Return new value
        return tic_total
    elif ticket_buy > 4:
        print('Please purchase only 4 tickets or less.')
        return tic_total
    else:
        print('Invalid input. Please try again.')
        return tic_total

main()