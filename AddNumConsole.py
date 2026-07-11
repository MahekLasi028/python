def Add(no1,no2):
    return  no1 + no2
    
def main():
    Ret1 = int(input("Enter  number 1 :"))
    Ret2 = int(input("Enter  number 2 :"))
    Result = Add(Ret1, Ret2)
    print("Addition is :", Result)
    
if __name__ == "__main__":
    main()
