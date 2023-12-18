class Vehicle(ABC):
    def __init__(self,now):
        self.now=now
    
    @abstractmethod
    def start(self):
        pass
    
class Bike(Vehicle):
    def start(self):
        print("Kick start")

class Car(Vehicle):
    def start(self):
        print("self start")

class Bus(Vehicle):
    def start(self):
        print("lever start")
        
b=Bike(2)
c=Car(4)
b2=Bus(6)
b.start()
c.start()
b2.start()
