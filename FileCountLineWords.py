def CountWords(filename):
    file = open(filename,"r")

    count = 0

    for line in file:
        words = line.split()
        count = count + len(words)
    
    file.close()
    return count

def main():
    name = input("Enter file name:")

    Ret = CountWords(name)

    print("Total no words in file are : ",Ret)

if __name__ == "__main__":
    main()
    
