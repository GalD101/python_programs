def idk():
    NUMBER_OF_ROWS = 3
    board = list()
    row = list()
    print("Please enter the board")
    for x in range(NUMBER_OF_ROWS):  # pylint: disable = unused-variable
        row = list()
        line = input()
        for digit in line:
            row.append(int(digit))
        board.append(row)
    print('[' + ',\n'.join([str(r) for r in board]) + ']')

        
idk()
