txt = input("Enter a word:").lower().replace(" ", "")
if txt[:-1] == txt[-1:0:-1]:
    print(True)
else:
    print(False)