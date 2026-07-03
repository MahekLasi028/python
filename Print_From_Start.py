def Print(no):
    print(12*"-", "Numbers are : ", 12*"-")
    for i in range(1, no + 1):
            print(i)

def main():
    
    no = int(input("Enter a number: "))
    Print(no)

if __name__ == "__main__":
    main()