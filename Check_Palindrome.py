def Palindrome(no):
    print(12*"-","Check Palindrome no ",12*"-")
    original = no
    reverse = 0
    while no!= 0:
        rem = no % 10
        reverse = reverse * 10 + rem
        no = no // 10
    if original == reverse:
        return True
    else:
        return False
def main():
    no = int(input("Enter no: "))
    
    if Palindrome(no):
        print(no, "is a palindrome number")
    else:   
        print(no, "is not a palindrome number")


if __name__ == "__main__":
    main()
 
   