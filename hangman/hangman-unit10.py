import random

HANGMAN_ASCII_ART = ("""  _    _
 | |  | |
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
 |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                      __/ |
                     |___/""")
MAX_TRIES = 6
RANDOM_IND = 0
WRONG_ANSWER = ':('
CORRECT_ANSWER = ':)'
hangman_photos = {
    0: "x-------x",
    1: """x-------x
|
|
|
|
|""",
    2: """x-------x
|       |
|       0
|
|
|""",
    3: """x-------x
|       |
|       0
|       |
|
|""",
    4: """x-------x
|       |
|       0
|      /|\\
|
|""",
    5: """x-------x
|       |
|       0
|      /|\\
|      /
|""",
    6: """x-------x
|       |
|       0
|      /|\\
|      / \\
|"""
}


def check_win(secret_word, old_letters_guessed):
    """Checks if the old_letters_guessed list contains all the letters in the secret_word
    :param secret_word: the secret word
    :param old_letters_guessed: all the letters that were guessed
    :type secret_word: string
    :type old_letters_guessed: list
    :return: The corresponding value if all the letters in the
    secret_word appear in the old_letters_guessed list
    :rtype: boolean
    """
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True


def show_hidden_word(secret_word, old_letters_guessed):
    """Calculates which letters were guessed correctly and display them
    in the string that represents the secret word
    :param secret_word: the secret word
    :param old_letters_guessed: all the letters that were guessed
    :type secret_word: string
    :type old_letters_guessed: list
    :return: The secret word displaying only the letters that are in old_letters_guessed list
    :rtype: string
    """
    UNDER_LINE = '_'
    SPACE = ' '
    hidden_word = secret_word
    for letter in secret_word:
        if letter not in old_letters_guessed:
            hidden_word = hidden_word.replace(letter, UNDER_LINE)
    return SPACE.join(hidden_word)


def check_valid_input(letter_guessed, old_letters_guessed):
    """Checks whether the input is valid (a single letter) and if it wasn't guessed before
    :param letter_guessed: the guess to check
    :param old_letters_guessed: a list of all the letters that were guessed
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: The corresponding value (True or False) if the letter is valid or not
    :rtype: boolean
    """
    return (letter_guessed.isalpha()) and (not len(letter_guessed) >= 2) \
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
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    print(FAILED)
    return False


def print_previous_guesses(old_letters_guessed):
    """Prints a sorted list of the previous guesses in arrow format
    :param old_letters_guessed: a list that contains all of the previous guesses
    :type old_letters_guessed: list
    :return: None
    """
    ARROW = "-> "
    print(ARROW.join(sorted(old_letters_guessed)))
    return None


def choose_word(file_path, index):
    """Finds the word in the corresponding index
    :param file_path: the path to the file with the words
    :param index: used to find a secret word by it's index
    :type file_path: string
    :type index: int
    :return: The secret word according to the index
    :rtype: string
    """
    words_file = open(file_path, 'r')
    words_list = list()
    secret_word = ""
    for text in words_file:
        words_list = text.split(' ')
    secret_word = words_list[index % len(words_list) - 1]
    return secret_word.lower()


def main():
    num_of_tries = 0
    secret_word = ""
    old_letters_guessed = list()

    # Print the welcome screen
    print(HANGMAN_ASCII_ART, "\n", MAX_TRIES)
    file_path = input("Enter file path: ")
    secret_word_index = int(
        input("Enter index (%d for a random index): " % RANDOM_IND))

    # Find the secret word with the index
    if secret_word_index == RANDOM_IND:
        random_number = random.randint(0, 999)
        secret_word = choose_word(file_path, random_number)
    else:
        secret_word = choose_word(file_path, secret_word_index)

    # Game start
    print("\nLet's start!")
    print(hangman_photos[num_of_tries])
    while (num_of_tries < MAX_TRIES) and not \
            check_win(secret_word, old_letters_guessed):
        print(show_hidden_word(secret_word, old_letters_guessed) + "\n")
        guess = input("Guess a letter: ").lower()
        if try_update_letter_guessed(guess, old_letters_guessed):
            if guess in secret_word:
                print(CORRECT_ANSWER)
            else:
                print(WRONG_ANSWER)
                num_of_tries += 1
                print(hangman_photos[num_of_tries])
        print_previous_guesses(old_letters_guessed)
    if num_of_tries == MAX_TRIES:
        print("LOSE")
        print("the word was: " + secret_word)
    else:
        print("\n" + show_hidden_word(secret_word, old_letters_guessed))
        print("WIN")


if __name__ == "__main__":
    main()
