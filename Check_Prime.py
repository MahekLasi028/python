def CheckPrime(no):
    print(12*"-","Check prime  no ",12*"-")
    is_prime = True
    for i in range(2, no):
        if no % i == 0:
            is_prime = False
            break
    if is_prime:
        print(no, "is a prime number")
    else:
        print(no, "is not a prime number")

def main():
    no = int(input("Enter no: "))
    CheckPrime(no)

if __name__ == "__main__":
    main()
   