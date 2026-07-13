class BankAccount:

    ROI = 10.5

    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account Holder Name : ",self.Name)
        print("Account Balanace : ",self.Amount)

    def Deposit(self):
        money = int(input("Enter the money to deposit:"))
        self.Amount=self.Amount + money
        print("Amount deposited successfully")

    def Withdraw(self):
        money = int(input("Enter the money to withdraw : "))
        if money <= self.Amount:
            self.Amount = self.Amount - money
            print("Withdraw successful..")
        else:
            print("Insufficient balance..")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) /100
        print("Interest : ",interest)

def main():
    obj1 = BankAccount("Mahek",10000)

    obj1.Display()
    obj1.Deposit()
    obj1.Withdraw()
    obj1.CalculateInterest()

if __name__== "__main__":
    main()

