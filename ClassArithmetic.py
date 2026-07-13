class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter Value 1:"))
        self.Value2 = int(input("Enter Value 2:"))

    def Addition(self):
        return self.Value1 + self.Value2
    
    def Substraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        return self.Value1 / self.Value2
    
Aobj1 = Arithmetic()
Aobj2 = Arithmetic()

Aobj1.Accept()
print("Addition is : ",Aobj1.Addition())
print("Multiplication is : ",Aobj1.Multiplication())
print("Substraction is : ",Aobj1.Substraction())
print("Division is : ",Aobj1.Division())

print()

Aobj2.Accept()
print("Addition is : ",Aobj2.Addition())
print("Multiplication is : ",Aobj2.Multiplication())
print("Substraction is : ",Aobj2.Substraction())
print("Division is : ",Aobj2.Division())