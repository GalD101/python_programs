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
if (len(user_guess) > 1) and (not user_guess.isalnum()):
    print("E3")
elif not user_guess.isalnum():
    print("E2")
elif  len(user_guess) > 1:
    print("E1")
else:
    print(user_guess)