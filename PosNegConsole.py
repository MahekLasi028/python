def ChkNum(no):

    if no>=0:
        return True
    else:
        return False

def main():

    Ret = int(input("Enter  number  :"))
    if(ChkNum(Ret)):
        print("Positive")
    else:
        print("Negative")
    
if __name__ == "__main__":
    main()
