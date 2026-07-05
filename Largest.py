Large = lambda no1 , no2 , no3 :no1 if no1 > no2 and no1 > no3 else no2 if no2 > no3 else no3

def main():
    num1 = int(input("Enter 1 st no :"))
    num2 = int(input("Enter 2nd no :"))
    num3 = int(input("Enter 3rd no :"))
    print(Large(num1, num2, num3))

if __name__ == "__main__":
    main()