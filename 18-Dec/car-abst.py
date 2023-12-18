from abc import ABC, abstractmethod
class Car(ABC):
    @abstractmethod
    def milage(self):
        pass
    
    def wheels(self):
        print("4 wheels")
        
class Tata(Car):
    def milage(self):
        print("Tata Mileage is 35")

class Maruti(Car):
    def milage(self):
        print("Maruti Mileage is 31")       
        
class Ford(Car):
    def milage(self):
        print("Ford Mileage is 49")
        
        
t=Tata()
m=Maruti()
f=Ford()
t.milage()
m.milage()
f.milage()
f.wheels()
