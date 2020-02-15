def main():
    path = input("Enter a file path: ")
    function_key_word = input("Enter a task: ")
    file = open(path, 'r')
    if function_key_word.lower() == "sort":
        list_of_words = list()    
        for line in file:
            for word in line.split():
                if word not in list_of_words:
                    list_of_words.append(word)
        list_of_words.sort()
        print(list_of_words)
    elif function_key_word.lower() == "rev":
        for line in file:
            print(line[::-1])
    elif function_key_word.lower() == "last":
        n = int(input("Enter a number"))
        for line in (file.readlines()[-n:]):
            print(line, end='')
    file.close()







if __name__ == "__main__":
    main()
