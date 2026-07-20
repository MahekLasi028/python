def CopyFile(source , destination):
    file1 = open(source,"r")
    file2 = open(destination,"w")

    for line in file1:
        file2.write(line)

    file1.close()
    file2.close()

def main():
    name1 = input("Enter source file name :")
    name2 = input("Enter destination file name")

    CopyFile(name1,name2)

    print("Contents copied successfully..")

    print("Contents of destiantion file are--")

    file = open(name2,"r")
    
    for line in file:
        print(line,end=" ")

    file.close()

if __name__ == "__main__":
    main()
