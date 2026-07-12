from multiprocessing import Pool
import os

def CountEven(no):
    count = 0

    for i in range(1, no + 1, 2):
        count = count + 1

    print("Process ID :", os.getpid())
    print("Input Number :", no)
    print("Even Number Count :", count)
    print()

    return count

def main():
    data = [1000000, 2000000, 3000000, 4000000]

    p = Pool()

    result = p.map(CountEven, data)

    p.close()
    p.join()

if __name__ == "__main__":
    main()