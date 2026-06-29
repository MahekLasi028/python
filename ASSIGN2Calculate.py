no1=int(input("Enter no 1:"))
no2=int(input("Enter no 2:"))
sum=no1+no2
sub=no1-no2
mul=no1*no2
if no2!=0:
    div=no1/no2
else:
    print("Cannot divide by zero")
print("ADD: ",sum)
print("SUB: ",sub)
print("MUL: ",mul)
print("DIV: ",div)
