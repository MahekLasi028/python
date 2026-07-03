def Cal(no1,no2):
    print("Addition of two numbers is: ",no1+no2)
    print("Subtraction of two numbers is: ",no1-no2)
    print("Multiplication of two numbers is: ",no1*no2)
    print("Division of two numbers is: ",no1/no2)

def main():
    no1 = int(input("Enter first number: "))
    no2 = int(input("Enter second number: "))
    Cal(no1, no2)

if __name__ == "__main__":
    main()