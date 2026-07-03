def ReverseOfDigit(no):
    print(12*"-","Reverse of digit in no ",12*"-")
    reverse = 0
    while no!= 0:
        rem = no % 10
        reverse = reverse * 10 + rem
        no = no // 10
    print("Reverse of digit in number is: ", reverse)

def main():
    no = int(input("Enter no: "))
    ReverseOfDigit(no)

if __name__ == "__main__":
    main()
 
   