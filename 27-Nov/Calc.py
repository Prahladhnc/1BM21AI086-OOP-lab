class Calc:
    def __init__(self, version):
        self.version = version
    
    def display(self):
        print("Version is:", self.version)
        
    @staticmethod
    def addNum(num1, num2):
        print(num1 + num2)
        
if __name__ == '__main__':   
    c1=Calc("casio 1")
    c2=Calc("Numero 2.9")
    c1.display() 
    c2.display()
    Calc.addNum(3,6)   
