from multiprocessing import Pool

def isPrime(no):
    if no<=1:
        return False
    
    for i in range(2,no):
        if no % i == 0:
            return False
        
    return True

def CountPrime(no):
    count = 0

    for i in range(2,no+1):
        if isPrime(i):
            count += 1

    return count

def main():
    data = [10000,20000,30000,40000]

    p = Pool()

    result = p.map(CountPrime,data)

    p.close()
    p.join()

    for i in range(len(data)):
        print("Prime count between 1 and ",data[i]," = ",result[i])

if __name__ =="__main__":
    main()


        
