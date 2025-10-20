# Alexander Masucci, Assignment #7
# Paragraph Sentence Counter

import re

# Gets sentences in a paragraph.
def getSentence(paragraph):

    # Defines the structure of a sentence. First letter capital (or a number),
    # any number of characters between, ends with punctuation.
    structure = r'[A-Z,0-9].*?[.!?‽](?= [A-Z]|$)'

    # Find all sentences in the paragraph.
    sen = re.findall(structure, paragraph, flags=re.DOTALL
                     | re.MULTILINE)
    return sen

def main():

    # Set up infinte while loop to be broken later.
    while True:

        print('Please type any paragraph. Please be sure to '
              'use proper capitalization and spelling.')
        paragraph = input()

        # Get sentences from paragraph.
        sen = getSentence(paragraph)

        # Print amount of sentences.
        print(f'Your paragraph has {len(sen)} sentences.')

        # If none found, remind user of grammar rules.
        if len(sen) == 0:
            print('Your sentences are likely missing punctuation or '
                  'fail to follow capitalization rules.')

        # Prints each sentence as a bullet point.
        for i in sen:
            print('•', i)
        print()

        # continue loop or not.
        while True:
            cont = str.lower(input('Continue? (y/n): '))
            if cont == 'y' or cont == 'yes':
                print()
                break
            elif cont == 'n' or cont == 'no':
                quit()
            else:
                print('Please answer with "y" or "n" only.')


main()