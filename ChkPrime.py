def ChkPrime(no):
    if no<=1:
        return False
    for i in range(2,no):
        if no % i == 0:
            return False
    return True

def main():
    num = int(input("Enter no :"))

    if ChkPrime(num):
        print(f"{num} is prime no ")
    else:
        print(f"{num} is not prime no ")

if __name__ =="__main__":
    main()

    