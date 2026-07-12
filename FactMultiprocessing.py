from multiprocessing import Pool
import os

def factorial(no):
    Fact = 1

    for i in range(1,no+1):
        Fact = Fact * i

    print("Process ID : ",os.getpid())
    print("Input no : ",no)
    print("Factorial : ",Fact)
    print()

    return Fact

def main():
    data =[10,15,20,25]

    p=Pool()

    result= p.map(factorial,data)

    p.close()
    p.join()

if __name__ =="__main__":
    main()
    
        
