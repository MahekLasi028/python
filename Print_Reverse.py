def PrintRev(no):
    print(12*"-", "Numbers are : ", 12*"-")
    for i in range(no,0,-1):
            print(i)

def main():

    no = int(input("Enter a number: "))
    PrintRev(no)

if __name__ == "__main__":
    main()