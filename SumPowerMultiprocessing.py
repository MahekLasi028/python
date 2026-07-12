from multiprocessing import Pool
import time

def SumPower(no):
    sum = 0

    for i in range(1, no+1):
        sum = sum +(i**5)

    return sum

def main():

    start = time.perf_counter()

    data=[1000000,2000000,3000000,4000000]

    p = Pool()

    result = p.map(SumPower,data)

    p.close()
    p.join()

    print(result)

    end = time.perf_counter()

    print("Total Execution time : ",end-start," seconds")

if __name__=="__main__":
    main()
