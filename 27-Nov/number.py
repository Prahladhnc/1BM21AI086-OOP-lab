class Number:
    def __init__(self, n=0.00):
        self.n=n
    def isprime(self):
        num=self.n
        if num > 1:
            for i in range(2, int(num/2)+1):
                if (num % i) == 0:
                    print(num, "is not a prime number")
                    return False
                    break
            else:
                print(num, "is a prime number")
                return True
        else:
            print(num, "is not a prime number")
            return False
        
    def ispos(self):
        if self.n > 0:
            return True
        return False
    
    def isneg(self):
        if self.n <0:
            return True
        return False
    
    def iszero(self):
        if self.n==0:
            return True
        return False
    
    def isodd(self):
        if (self.n)%2==1:
            return True
        return False
    
    def iseven(self):
        if (self.n)%2==0:
            return True
        return False
    
    def getsqrt(self):
        return (self.n)**0.5
    
    def getsqr(self):
        return(self.n)**2
    
x=Number(33.442)
print(x.getsqrt())
print(x.getsqr())
print(x.isneg())
print(x.ispos())
print(x.isprime())
