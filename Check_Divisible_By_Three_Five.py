def Divisible(no):
    if no % 3 == 0 and no % 5 == 0:
        print("Number is divisible by both 3 and 5")
    elif no % 3 == 0:
        print("Number is divisible by 3")
    elif no % 5 == 0:
        print("Number is divisible by 5")
    else:
        print("Number is not divisible by either 3 or 5")

def main():
    no = int(input("Enter number:"))
    Divisible(no)

if __name__ == "__main__":
    main()