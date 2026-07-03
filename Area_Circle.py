def Area(pi,r):
    return pi*r*r

def main():
    radius = float(input("Enter the radius: "))
    Ret = Area(3.14,radius)
    print(f"The area of the circle is: {Ret}")

if __name__ == "__main__":
    main()