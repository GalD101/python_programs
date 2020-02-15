# TODO add documentation for all functions
# 5.3.4

# -------- Self.py --------


import sys
import functools


def last_early(my_str):
    return (len(my_str) > 1) and (my_str[:-1].lower().count(my_str[-1]) != 0)

# 5.3.5


def distance(num1, num2, num3):
    first_condition = ((abs(num2 - num1) == 1) or (abs(num3 - num1) == 1)
                       ) and not ((abs(num2 - num1) == 1) and (abs(num3 - num1) == 1))
    # FIXME adjust second_condition
    second_condition = ((abs(num2 - num1) >= 2) or (abs(num2 - num3) >= 2)) or (abs(
        num3 - num1) >= 2) and not ((abs(num2 - num1) >= 2) and (abs(num2 - num3) >= 2))
    return first_condition and second_condition

# 5.3.6


def filter_teens(a=13, b=13, c=13):
    a = fix_age(a)
    b = fix_age(b)
    c = fix_age(c)
    return a + b + c


def fix_age(age):
    if age >= 13 and age <= 19 and (age != 15 and age != 16):
        age = 0
    return age

# 5.3.7


def chocolate_maker(small, big, x):
    if x % 5 == 0:
        return x <= big * 5 + small
    elif 5 * big + small > x:
        return x % 5 <= small
    return small + 5 * big == x

# 5.4.1


def func(num1, num2):
    """Calculates the absolute value of the difference between the two numbers
    :param num1: number
    :param num2: number
    :type num1: int
    :type num2: int
    :return: The absolute value of the difference between num1 and num2
    :rtype: int
    """
    return abs(num2 - num1)

# 6.1.2


def shift_left(my_list):
    my_list[0], my_list[1], my_list[2] = my_list[1], my_list[2], my_list[0]
    return my_list

# 6.2.3


def format_list(my_list):
    formatted_list = my_list[:-1:2]
    seperator = ', '
    print(seperator.join(formatted_list), 'and', my_list[-1])

# 6.2.4


def extend_list_x(list_x, list_y):
    list_x = list_y.__add__(list_x)
    return list_x

# 6.3.1


def are_lists_equal(list1, list2):
    list1_sorted = sorted(list1)
    list2_sorted = sorted(list2)
    return list1_sorted == list2_sorted

# 6.3.2


def longest(my_list):
    return max(my_list, key=len)

# 7.1.4


def squared_numbers(start, stop):
    list_of_squared_numbers = list()
    while start <= stop:
        list_of_squared_numbers.append(start ** 2)
        start += 1
    return list_of_squared_numbers

# 7.2.1


def is_greater(my_list, n):
    greater_list = list()
    for num in my_list:
        if num > n:
            greater_list.append(num)
    return greater_list

# 7.2.2


def numbers_letters_count(my_str):
    """Counts how many letters are in a given string and \
    how many numbers are in the string
    :param my_str: a string to check
    :type my_str: string
    :return: The number of letters and the number of numbers in the string
    :rtype: list
    """
    letters_count = 0
    numbers_count = 0
    for char in my_str:
        if char.isdigit():
            numbers_count += 1
        else:
            letters_count += 1
    return [numbers_count, letters_count]

# 7.2.4


def seven_boom(end_number):
    BOOM = "BOOM"
    KEY_NUMBER = '7'
    number_series = list()
    for num in range(end_number):
        if (num % 7 == 0) or (KEY_NUMBER in str(num)):
            number_series.append(BOOM)
            continue
        number_series.append(num)
    return number_series

# 7.2.5


def sequence_del(my_str):
    if len(my_str) <= 1:
        return my_str
    previous_char = my_str[0]
    i = 1
    current = my_str[i]
    finished = False
    # FIXME adjust function to be more efficient
    while not finished:
        if current == previous_char:
            my_str = remove_at(i, my_str)
            finished = i == len(my_str)
            if finished:
                break
            previous_char = my_str[i]
            continue
        previous_char = my_str[i]
        i += 1
        finished = i == len(my_str)
        if finished:
            break
        current = my_str[i]
    return my_str
    # return (''.join(sorted(set(my_str), key=my_str.index)))


def remove_at(i, s):
    return s[:i] + s[i+1:]


def remove_from_i_to_j(i, j, s):
    k = i
    while k <= j:
        s = remove_at(i, s)
        k += 1
    return s

# 7.2.6
# TODO make function more user friendly


def shopping_list():
    COMMA = ','
    s_list = list()
    list_str = input("Please enter your shopping list: ")
    i = 0
    while i < (list_str.count(COMMA)):
        s_list.append(list_str[:list_str.find(COMMA)])
        list_str = remove_from_i_to_j(0, list_str.find(COMMA), list_str)
    s_list.append(list_str)
    action_code = 0
    while action_code != 9:
        action_code = int(input("""Please enter action code
        1 print the list
        2 return the number of products
        3 check if a certain product is in the list
        4 return how many times a certain product appears in the list
        5 delete a product from the list
        6 add a product to the list
        7 print all illegal products
        8 remove duplicates
        9 quit
        """))
        if action_code == 1:
            for product in s_list:
                print(product)
        elif action_code == 2:
            print(len(s_list))
        elif action_code == 3:
            is_in_list = False
            product_name = input("Enter product name")
            for product in s_list:
                if product == product_name:
                    is_in_list = True
                    break
            print(is_in_list)
        elif action_code == 4:
            num_of_occurrences = 0
            product_name = input("Enter product name")
            for product in s_list:
                if product == product_name:
                    num_of_occurrences += 1
            print(num_of_occurrences)
        elif action_code == 5:
            product_to_delete = input("Enter product to delete from the list")
            if s_list.__contains__(product_to_delete):
                s_list.remove(product_to_delete)
                print("Successfully deleted")
            else:
                print("Product not found")
        elif action_code == 6:
            s_list.append(input("Enter product to add to the list"))
        elif action_code == 7:
            for product in s_list:
                if len(product) < 3 or not product.isalpha():
                    print(product)
        elif action_code == 8:
            res = list()
            for prod in s_list:
                if prod not in res:
                    res.append(prod)
            s_list = res

# 7.2.7


def arrow(my_char, max_length):
    my_arrow = ""
    for i in range(max_length):
        for j in range(i):  # pylint: disable = unused-variable
            my_arrow += my_char
        my_arrow += "\n"
    for i in range(max_length, 0, -1):
        for j in range(i):
            my_arrow += my_char
        my_arrow += "\n"
    return my_arrow


def sort_prices(list_of_tuples):
    list_of_tuples = (sorted(list_of_tuples,
                             key=lambda price: float(price[1])))
    list_of_tuples.reverse()
    return list_of_tuples


# 8.2.2 function using bubble sort
def sort_prices2(list_of_tuples):
    for i in range(len(list_of_tuples)):
        for j in range(0, len(list_of_tuples) - i - 1):
            if list_of_tuples[j][1] < list_of_tuples[j+1][1]:
                list_of_tuples[j], list_of_tuples[j +
                                                  1] = list_of_tuples[j+1], list_of_tuples[j]
    return list_of_tuples


# 8.2.3
def mult_tuple(tuple1, tuple2):
    final_tuple = tuple()
    new_tuple1 = tuple()
    new_tuple2 = tuple()
    for i in tuple1:
        for j in tuple2:
            new_tuple1 = ((i, j), )
            new_tuple2 = ((j, i), )
            final_tuple = final_tuple.__add__(new_tuple1)
            final_tuple = final_tuple.__add__(new_tuple2)
    return final_tuple


# 8.2.4
def sort_anagrams(list_of_strings):
    is_anagram = True
    first_time = True
    f = True
    list_of_anagram_words = list()
    anagram_word = ""
    counter = 0
    words_to_delete = list()
    word = ""
    temp_list = list()
    for word in list_of_strings:
        # FIXME change so will work even if two anagram words appear in sequence
        for w in words_to_delete:
            if w in list_of_strings:
                list_of_strings.remove(w)
        if not f:
            list_of_anagram_words.append(temp_list)
        word_check = word
        first_time = True
        # Temp list to contain the word we check
        temp_list = list()
        temp_list.append(word_check)
        for word2 in list_of_strings:
            counter = 0
            for char in word:
                first_time = False
                is_anagram = True
                if char not in word2 or word == word2:
                    is_anagram = False
                    break
                else:
                    counter += 1
                    anagram_word = word2
                if is_anagram and not first_time and counter == len(word):
                    temp_list.append(anagram_word)
                    # Save elements that are anagram to word_check in order to delete in the next iteration (prevent dups)
                    words_to_delete.append(anagram_word)
                    f = False

    return list_of_anagram_words

# 8.3.3


def count_chars(my_str):
    my_str = my_str.replace(' ', '')
    len_of_str = len(my_str)
    letter_index = 0
    dict_of_str = dict()
    while letter_index < len_of_str:
        letter = my_str[letter_index]
        letter_count = my_str.count(letter)
        my_str.replace(letter, "")
        len_of_str = len(my_str)
        dict_of_str[letter] = letter_count
        letter_index += 1
    return dict_of_str


# 8.3.4


def inverse_dict(my_dict):
    # TODO write function
    pass

# 9.1.1


def are_files_equal(file1, file2):
    f1 = open(file1, 'r')
    f2 = open(file2, 'r')
    return f1.read() == f2.read()


def copy_file_content(source, destination):
    source_file = open(source, 'r')
    destination_file = open(destination, 'w')
    source_contant = source_file.read()
    destination_file.write(source_contant)


def who_is_missing(file_name):
    # TODO write function
    pass


def my_mp3_playlist(file_path):
    SEMICOLON = ';'
    playlist_file = open(file_path, 'r')
    max_minutes = 0
    max_seconds = 0
    num_of_songs = 0
    performer_name = list()
    for line in playlist_file:
        length = line.split(SEMICOLON)[2]
        performer_name.append(line.split(SEMICOLON)[1])
        num_of_songs += 1
        minutes, seconds = length.split(':')
        if int(minutes) >= max_minutes:
            if int(seconds) > max_seconds:
                longest_song = line[:line.find(SEMICOLON)]
                max_minutes = int(minutes)
                max_seconds = (seconds)
    counter = 0
    most_appearances = performer_name[0]

    for name in performer_name:
        num_of_appearances = performer_name.count(name)
        if(num_of_appearances > counter):
            counter = num_of_appearances
            most_appearances = name
    return longest_song, num_of_songs, most_appearances


def my_mp4_playlist(file_path, new_song):
    # TODO write function
    pass


def integer(a, m):
    if a >= m:
        return 1 + integer(a - m, m)
    else:
        return 0


# -------- Next.py --------

# 1.1.2
def double_letter(my_str):
    return ''.join(map(lambda x: 2 * x, my_str))

# 1.1.3


def four_dividers(number):
    return list(filter(lambda x: x % 4 == 0, range(1, number)))

# 1.1.4


def sum_of_digits(number):
    return functools.reduce(lambda a, b: a + b, map(int, str(number)))


def combine_coins(coin, numbers):
    return ', '.join(map(lambda s, n: s + str(n), [coin for i in numbers], numbers))

# 1.3.1


def intersection(list_1, list_2):
    return list(set([x for x in list_1 if x in list_2]))

# 1.3.2


def is_prime_one_line(number):
    # TODO write function in one line (use list comperhension and reduce, map or filter)
    pass


# 1.3.3


def is_funny(string):
    return (lambda b: not False in b)(([True if letter == 'a' or letter == 'h'
                                        else False for letter in string]))

# 1.3.2


def caesar_shift(shift, password):
    return (''.join((chr(ord(letter) + shift) for letter in password)))


# 1.5
def longest_word_in_file(file_path):
    return functools.reduce(lambda word1, word2: max([word1, word2], key=len), open(file_path, 'r'))


def total_length_of_words_in_file(file_path):
    return len([letter for word in open(file_path, 'r') for letter in word if letter != '\n'])


def shortest_words_in_file(file_path):
    list_of_words = [word if word[-1] != '\n' else word[:-1]
                     for word in open(file_path, 'r')]
    len_of_short_word = len(functools.reduce(lambda word1, word2: min(
        [word1, word2], key=len), open(file_path, 'r')))
    return '\n'.join(filter(lambda word: len(word) == len_of_short_word, list_of_words))


def create_file_with_len_of_each_word(file_path):
    list_of_words_len = [str(len(word)) if word[-1] != '\n' else str(len(word[:-1]))
                         for word in open(file_path, 'r')]
    new_file = open(file_path[0:file_path.find(
        '.txt')] + '_len_of_each_word.txt', 'w')
    new_file.write('\n'.join(list_of_words_len))
    print('new file at ' +
          file_path[0:file_path.find('.txt')] + '_len_of_each_word.txt')


def get_names_by_length(file_path):
    n = int(input("Enter name length: "))
    return '\n'.join(filter(lambda word: len(word) == n, [word if word[-1] != '\n'
                                                          else word[:-1] for word in open(file_path, 'r')]))


def read_file(file_name):
    try:
        print("__CONTENT_START__")
        with open(file_name, 'r') as txt_file:
            print(txt_file.read())
    except FileNotFoundError:
        print("__NO_SUCH_FILE__")
    else:
        txt_file.close()
    finally:
        print("__CONTENT_END__")


def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in',
             'gato': 'cat', 'casa': 'house', 'el': 'the'}
    translated_sentence = (words[word] for word in sentence.split())
    for translated_word in translated_sentence:
        print(translated_word, end=' ')


def is_prime(n):
    # Corner case
    if n <= 1:
        return False

    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def first_prime_over(n):
    g = (next_prime for next_prime in range(
        n, sys.maxsize**10) if is_prime(next_prime))
    return next(g)


def permutate(seq):
    """permutate a sequence and return a list of the permutations"""
    if not seq:
        return [seq]  # is an empty sequence
    else:
        temp_perm = []
        for i in range(len(seq)):
            part = seq[:i] + seq[i+1:]
            for p in permutate(part):
                temp_perm.append(seq[i:i+1] + p)
        return temp_perm


def main():
    # return functools.reduce(lambda a, b: a + b, [len(word) - 1 if word[-1] == '\n' else len(word) \
    #    for word in open(file_path, 'r')])
    # 8.2.1
    # data = ("self", "py", 1.543)
    # format_string = "Hello %s.%s learner, you have only %.1f units left before you master the course!"
    # print(format_string % data)

    # kd = (3,5)
    # seven = (7,)
    # kd = kd.__add__(seven)
    # print(kd)

    # first_tuple = (1, 2, 3)
    # second_tuple = (4, 5, 6)
    # mult_tuple(first_tuple, second_tuple)

    # 8.2.2
    # products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
    # print(sort_prices(products))

    # products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
    # print(sort_prices(products))

    # list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating',
    #                 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
    # print(sort_anagrams(list_of_words))

    # copy_file_content(r"C:\Users\User\Desktop\copy.txt", r"C:\Users\User\Desktop\paste.txt")
    # print(integer(14, 5))

    # print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5, 6])))

    # print(sum_of_digits(104))

    # print(combine_coins('$', range(5)))

    # print(intersection([1, 2, 3, 4], [8, 3, 9]))
    # print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))

    # print(is_funny("hahaha"))

    # g = ""
    # for i in range(len(password)):
    #    g += (chr(ord(password[i]) + 2))
    # print(g)

    # password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
    # print(caesar_shift(2, password))

    # print(create_file_with_len_of_each_word(
    #     r'C:/Users/User/Desktop/names.txt'))
    # print(get_names_by_length(r'C:/Users/User/Desktop/names.txt'))
    # print(first_prime_over(1000000))
    #chr((ord(i) + shift) % 26)


if __name__ == "__main__":
    main()