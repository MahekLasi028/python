def CountLines(filename):
    file = open(filename,"r")

    count = 0

    for line in file:
        count = count + 1
    
    file.close()
    return count

def main():
    name = input("Enter file name:")

    Ret = CountLines(name)

    print("Total no lines in file are : ",Ret)

if __name__ == "__main__":
    main()
    
