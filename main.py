import arithmetic as ar

def main():
    No=int(input("Enter 1st no:"))
    No2=int(input("Enter 2nd no:"))

    print("Addition is : ",ar.Add(No,No2))
    print("Subtraction is : ",ar.  Sub(No,No2))
    print("Multiplication is : ",ar.Mul(No,No2))
    print("Division is : ",ar.Div(No,No2))

if __name__ == "__main__":
    main()