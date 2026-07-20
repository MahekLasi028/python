def squares(n):
    for i in range(1,n+1):
        yield i*i
gen = squares(5)
print(next(gen))
print(next(gen))
print(next(gen))


no = [45,78,50,56,77,34,35]
convert = list(filter(lambda x : x>50,no))
print(convert)

def sumAll(*args):
    return sum(args)
print(sumAll(45,343))



#generator  is used to genetare the output according to reuirements of user at dyanmic time
#yeild used to stop and the execution next used to genearte the values ..
def squares(n):
    for i in range(1,n+1):
        yield i*i
gen = squares(5)
print(next(gen))
print(next(gen))
print(next(gen))


def f(**kwargs):
    print(kwargs)
f(name="mHEK",name1="abc")