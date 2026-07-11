def fact(no):
    Fact = 1 
    for i in range(1,no+1,1):
        Fact = Fact * i
    return Fact

def main():
    Input =int(input("Enter no :"))
    Ret = fact(Input)
    print(Ret)

if __name__=="__main__":
    main()


