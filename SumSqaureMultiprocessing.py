from multiprocessing import Pool

def SumSquare(n):
    sum = 0

    for i in range(1,n+1):
        sum = sum+(i*i)

    return sum

def main():
    data = [100000,200000,300000,400000]

    p = Pool()

    result = p.map(SumSquare,data)

    p.close()
    p.join()

    print(result)

if __name__=="__main__":
    main()



