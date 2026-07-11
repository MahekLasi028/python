def ChkNum(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
def main():
    Ret = int(input("Enter a number :"))
    ChkNum(Ret)
if __name__ == "__main__":
    main()
