def choose_word(file_path, index):
    """Calculates the number of words in the file
    and finds the word in the corresponding index
    :param file_path: the path to the file with the words
    :param index: used to find a secret word by it's index
    :type file_path: string
    :type index: int
    :return: The number of words in a file
    and the secret word according to the index
    :rtype: tuple (int, string)
    """ 
    songs_file = open(file_path, 'r')
    songs_list = list()
    secret_word = ""
    for text in songs_file:
        songs_list = text.split(' ')
    secret_word = songs_list[index % len(songs_list) - 1]
    no_dups_songs = list()
    for song in songs_list:
        if song not in no_dups_songs:
            no_dups_songs.append(song)
    songs_list = no_dups_songs
    return len(no_dups_songs), secret_word


print(choose_word(r'C:\Users\User\Desktop\words.txt', 15))
