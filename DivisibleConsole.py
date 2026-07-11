def Divisibe(no):

    if no % 5 ==0:
        return True
    else:
        return False

def main():

    Ret = int(input("Enter  number  :"))
    if(Divisibe(Ret)):
        print("Divisible by 5")
    else:
        print("Not divisible by 5")
    
if __name__ == "__main__":
    main()
