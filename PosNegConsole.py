def ChkNum(no):

    if no>0:
        return True
    elif no==0:
        return "Zero"
    else:
        return False

def main():

    Ret = int(input("Enter  number  :"))
    if ChkNum(Ret) == True:
        print("Positive")
    elif ChkNum(Ret) == "Zero":
        print("Zero")
    else:
        print("Negative")
    
if __name__ == "__main__":
    main()
