def SumOfDigit(no):
    print(12*"-","Sum of digit in no ",12*"-")
    Sum = 0
    while no!= 0:
        rem = no % 10
        Sum = Sum + rem
        no = no // 10
    print("Sum of digit in number is: ", Sum)

def main():
    no = int(input("Enter no: "))
    SumOfDigit(no)

if __name__ == "__main__":
    main()
   