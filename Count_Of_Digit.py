def CountOfDigit(no):
    print(12*"-","Count of digit in no ",12*"-")
    count = 0
    while no!= 0:
        count += 1
        no = no // 10
    print("Count of digit in number is: ", count)

def main():
    no = int(input("Enter no: "))
    CountOfDigit(no)

if __name__ == "__main__":
    main()
   