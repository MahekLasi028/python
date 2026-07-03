def Sum(no):
    print(12*"-","Sum of 1st n natural nos",12*"-")
    Sum = 0
    for i in range(no+1):
        Sum = Sum + i
    print("Sum of 1st n natural numbers is: ", Sum)

def main():
    no = int(input("Enter no: "))
    Sum(no)

if __name__ == "__main__":
    main()
   