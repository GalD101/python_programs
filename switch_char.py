KEY_LETTER = 'e'
message = input("Please enter a string:")
first_letter = message[0]
message = first_letter + message[1:].replace(first_letter, KEY_LETTER)
print(message)