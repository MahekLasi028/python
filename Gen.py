#generator  is used to genetare the output according to reuirements of user at dyanmic time
#yeild used to stop and the execution next used to genearte the values ..
def squares(n):
    for i in range(1,n+1):
        yield i*i
gen = squares(5)
print(next(gen))
print(next(gen))
print(next(gen))

def even(n):
    for i in range(1,n+1):
        if i % 2 == 0:
            yield i
gen1 = even(5)
print(next(gen1))
print(next(gen1))


