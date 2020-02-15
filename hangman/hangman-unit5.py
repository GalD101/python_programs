def is_valid_input(letter_guessed):
    """Checks if the input is a single letter
    :param letter_guessed: input to check
    :type letter_guessed: string
    :return: True if the input is valid, false otherwise
    :rtype: boolean
    """
    return not ((len(user_guess) > 1) and (not user_guess.isalnum()) or \
        (not user_guess.isalnum()) or (len(user_guess) > 1))
HANGMAN_ASCII_ART = ("""  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                      __/ |                      
                     |___/""")
MAX_TRIES = 6
print(HANGMAN_ASCII_ART ,"\n", MAX_TRIES)
user_guess = input("Guess a letter: ").lower()
print(is_valid_input(user_guess))