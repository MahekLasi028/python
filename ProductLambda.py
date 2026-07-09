from functools import reduce
no = [ 10,20,30,40,50]
mul= reduce(lambda x, y: x * y, no)
print(mul)
