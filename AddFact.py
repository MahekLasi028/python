def Addfact(no):
    Fact = 0
    for i in range(1,no):
        if no % i == 0:
            Fact = Fact + i
    return Fact

def main():
    Input =int(input("Enter no :"))
    Ret = Addfact(Input)
    print("Addition of factors is :",Ret)

if __name__=="__main__":
    main()


