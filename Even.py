def Even(no):
    print(12*"-","Even  no ",12*"-")
    for i in range(1,no+1):
        if i%2 == 0:
            print(i)

def main():
    no = int(input("Enter no: "))
    Even(no)

if __name__ == "__main__":
    main()
   