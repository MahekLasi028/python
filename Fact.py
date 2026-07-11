def Fact(no):
    fact = 1 
    for i in range(1,no+1):
        fact = fact *i
    return fact
        

def main():
    Input = int(input("Enter no :"))
    Ret = Fact(Input)
    print("Factorial of no is  : ",Ret)

if __name__ == "__main__":
    main()