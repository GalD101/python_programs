message = input("Please enter a string:")
print(message[:len(message) // 2].lower() +
message[len(message) // 2:].upper())