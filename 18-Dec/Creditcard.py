class Creditcard():
    def __init__(self, acc, limit, bal):
        self.acc=acc
        self.__limit=limit
        self.__bal=bal
        
    def get_balance(self):
        print("Balance is ", self.__bal)
        
    def withdraw(self, amt):
        if amt>self.__limit:
            print("Limit exceeded")
        if amt>self.__bal:
            print("Balance exceeded")
        else:
            self.__bal-=amt
            print("Withdrawn")
    
    def deposit(self, amt):
        self.__bal+=amt
        print("Deposited")

c1=Creditcard("Ram", 2500, 3000)
c1.get_balance()
c1.withdraw(2700)
c1.withdraw(2200)
c1.withdraw(2000)
c1.deposit(2500)
     
