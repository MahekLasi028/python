from functools import reduce
numbers =[1,2,3,4,5]
max_num = reduce(lambda x,y : x if x>y else y,numbers)
print("Total : ",max_num)