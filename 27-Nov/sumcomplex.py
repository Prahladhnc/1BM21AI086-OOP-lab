class Complex:
    def __init__(self,r=0,c=0):
        self.real=r
        self.img=c
    
    def display(self):
        print(self.real, "+",self.img ,"i")
    
    def add(self,a,b):
        self.real=a.real+b.real
        self.img=a.img+b.img
        
if __name__=="__main__":
    c1=Complex(3,5)
    c2=Complex(2,-2)
    c3=Complex()
    c1.display()
    c2.display()
    c3.add(c1,c2)
    print("Sum of the 2 complex numbers")
    c3.display()
