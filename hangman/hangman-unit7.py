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
