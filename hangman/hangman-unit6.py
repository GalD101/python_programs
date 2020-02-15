def check_valid_input(letter_guessed, old_letters_guessed):
    """Checks whether the input is valid (a single letter) and if it wasn't guessed before
    :param letter_guessed: the guess to check
    :param old_letters_guessed: a list of all the letters that were guessed
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: The corresponding value (True or False) if the letter is valid or not
    :rtype: boolean
    """
    return (letter_guessed.isalpha()) and (not len(letter_guessed) >= 2)\
         and (not old_letters_guessed.__contains__(letter_guessed.lower()))

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """Adds the guess to the list of guesses if it's valid
    :param letter_guessed: the guess to add
    :param old_letters_guessed: a list of all the letters that were guessed
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: The corresponding value if the letter was added, if not, will \
        also print 'X' and the list of the previous guesses
    :rtype: boolean
    """
    FAILED = 'X'
    ARROW = "-> "
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    print(FAILED + "\n" + ARROW.join(old_letters_guessed))
    return False

# Optional
def print_previous_guesses(old_letters_guessed):
    """Prints the list of previous guesses in arrow format
    :param old_letters_guessed: a list that contains all of the previous guesses
    :type old_letters_guessed: list
    :return: None
    """
    ARROW = "-> "
    print(ARROW.join(old_letters_guessed))
    return None