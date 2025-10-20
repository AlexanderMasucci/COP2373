# Alexander Masucci, Assignment #2
# Spam Email Checker

# Main Function
def main():
    print("Spam Email Checker")

    # Initializing variables.
    loopbool = True
    email = "."
    # Tracks words that match the spam list.
    matched = []

    while loopbool != False:
        # Call functions
        email = get_email(email)
        matched = spam_scan(email, matched)
        spam_score(matched)
        print()

        # Ask again if user desires
        loopclose = input("Would you like to input another email? (y/n) ")
        loopclose = loopclose.lower()

        if loopclose == "y" or loopclose == "yes":
            print()
        else:
            loopbool = False

# Function gets email though user input.
def get_email(email):
    print("Please input the email.")
    email = input()
    email = email.lower()
    return email

# Checks message for common spam email phrases and adds them to a list.
def spam_scan(email, matched):
    print()
    print()
    print('Scanning...')
    print()

    # List of words commonly found in spam emails.
    spam_list = ["free", "gift", "100%", "cash", "money",
                 "act", "risk-free", "urgent", "virus",
                 "win", "winner", "multi-level", "password",
                 "bargain", "debt", "consultation", "giveaway",
                 "spam", "prize", "save", "money-back",
                 "member", "special", "breach", "violation",
                 "bet", "lottery", "miracle", "immediately"
                 "income" ]

    # Checks for each word in the spam list
    for word in spam_list:
        if word in email:
            matched.append(word)
    return matched

# Checks the "spam score" and tells the user if their email may be spam
def spam_score(matched):
    # Get total number of matching words.
    score = len(matched)

    # Several different responses based on number of matching words.
    if score == 0:
        print('This email is likely not spam.')
        return
    elif 0 < score < 3:
        print('Only a few words matched our filters. This email is '
              'likely not spam. However, be cautious.')
    elif 3 < score < 7:
        print('Some words matched our filters. This email may be spam. Proceed with caution and'
              ' do not click on suspicious links or attachments.')
    else:
        print('This email is likely spam. Do not click on any links or attachments.')

    print('These words matched our filters, which often indicate spam:')
    print(matched)



# Call main function
main()