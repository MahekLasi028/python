def SearhWord(filename,word):
    file = open(filename,"r")

    for line in file:
        if word in line:
            return True
            file.close()
    file.close()
    return False

def main():
    name = input("Enter name of file:")
    word = input("Enter the word to search:")

    Ret = SearhWord(name,word)

    if Ret:
        print("Word found..")
    else:
        print("Word not found")

if __name__ == "__main__":
    main()