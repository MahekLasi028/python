def pattern(no):
    for i in range(no):
        for j in range(no):
            print(" * ",end=" ")
        print()

def main():
    Input = int(input("Enter no :"))
    pattern(Input)

if __name__ == "__main__":
    main()