def Print_Table(no):
    print(12*"-","Multiplication Table",12*"-")
    for i in range(1,11):
        print(no," * ",i," =",no*i)

def main():
    no = int(input("Enter no: "))
    Print_Table(no)
if __name__ == "__main__":
    main()
   