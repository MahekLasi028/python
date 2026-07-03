def ChkGreater(no1, no2):
    if no1 > no2:
       print(no1, " is greater")
    elif no1 < no2:
       print(no2, " is greater")
    else:
         print("Both numbers are equal")

def main():
    no1 = int(input("Enter 1st no :"))
    no2 = int(input("Enter 2nd no :"))
    
    Ret = ChkGreater(no1 , no2)

if __name__ =="__main__":
    main()