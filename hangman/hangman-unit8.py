PIC0 = "x-------x"
PIC1 = """... x-------x
...    |
...    |
...    |
...    |
...    |"""
PIC2 = """... x-------x
...    |       |
...    |       0
...    |
...    |
...    |"""
PIC3 = """... x-------x
...    |       |
...    |       0
...    |       |
...    |
...    |"""
PIC4 = """... x-------x
...    |       |
...    |       0
...    |      /|\\
...    |
...    |"""
PIC5 = """... x-------x
...    |       |
...    |       0
...    |      /|\\
...    |      /
...    |"""
PIC6 = """... x-------x
...    |       |
...    |       0
...    |      /|\\
...    |      / \\
...    |"""
HANGMAN_PHOTOS = {"picture0": PIC0, "picture1": PIC1,
                  "picture2": PIC2, "picture3": PIC3,
                  "picture4": PIC4, "picture5": PIC5, "picture6": PIC6}


def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS["picture%d" % num_of_tries])