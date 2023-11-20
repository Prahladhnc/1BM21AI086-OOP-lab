class Dog:
    name=""
    size=""
    breed="Unknown"
    dob="Unknown"
    
    def __init__(self,name,size,age=0,breed="Unknown", dob="Unknown"):
        self.name=name
        self.size=size
        self.breed=breed
        self.age=age
        self.dob=dob
        self.age
    def bark(self):
        print(self.name,": woof")
    
    def get_name(self):
        print("My name is:", self.name) 
    
    def set_name(self, newname):
        n=len(newname)
        old=self.name
        if n<2:
            print("Name Too short")
        elif n>30:
            print("Name too long")
        else:
            newname.title()
            self.name=newname
            print("Name changed from: ", old, "to ", self.name)
            
    def dog_years(self):
        dogage=self.age * 7
        print("Dog age of ", self.name, "is", dogage)
        
dog=Dog("Tomy", "large",8, "Labrador")
print(dog.breed)
dog.bark()
dog.get_name()
dog2=Dog("pinky", "small", 4)
dog2.set_name("a")
dog.set_name('Browny')
dog.dog_years()
