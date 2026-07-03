def Odd(no):
    print(12*"-","Odd  no ",12*"-")
    for i in range(1,no+1):
        if i%2 == 1:
            print(i)

def main():
    no = int(input("Enter no: "))
    Odd(no)

if __name__ == "__main__":
    main()
   