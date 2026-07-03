def Fact(no):
    print(12*"-","Factorial of no ",12*"-")
    Fact = 1
    for i in range(1,no+1):
        Fact = Fact * i
    print("Factorial of number is: ", Fact)

def main():
    no = int(input("Enter no: "))
    Fact(no)

if __name__ == "__main__":
    main()
   