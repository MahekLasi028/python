def DisplayFile(filename):
    file = open(filename,"r")

    count = 0

    for line in file:
       print(line,end=" ")
    
    file.close()

def main():
    name = input("Enter file name:")

    print("-----DISPLAYING THE FILE CONTENTS------")
    DisplayFile(name)

if __name__ == "__main__":
    main()
    
