min = lambda no1 , no2 : no1 if no1 < no2 else no2

def main():
    n1 = int(input("Enter 1st no :"))
    n2 = int(input("Enter 2nd no :"))

    print("Min : ",min(n1,n2))

if __name__ == "__main__":
    main()