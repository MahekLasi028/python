def Area(l,w):
    return l * w

def main():
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    Ret = Area(length, width)
    print(f"The area of the rectangle is: {Ret}")

if __name__ == "__main__":
    main()