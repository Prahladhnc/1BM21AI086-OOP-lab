class birthdayboy:
    name="name"
    age=0
    
    def __init__(self,n,a):
        self.name=n
        self.age=a
    
    def birthday(self):
        self.age+=1

boy=birthdayboy("Vishnu",20)
print("Name: ", boy.name, "\nAge before birthday: ", boy.age)

boy.birthday()
print("Name: ", boy.name, "\nAge after birthday: ", boy.age)
