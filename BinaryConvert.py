def DecimalToBinary(no):
    binary = ""

    while no > 0:
        rem = no % 2
        binary = str(rem) + binary
        no = no // 2

    return binary

def main():
    no = int(input("Enter a number: "))

    if no == 0:
        print("Binary equivalent: 0")
    else:
        print("Binary equivalent:", DecimalToBinary(no))

if __name__ == "__main__":
    main()