class Student:
    count=0
    def __init__(self,n,m):
        self.marks=m
        self.name=n
        Student.count+=1
    def disp(self):
        print("Name: ",self.name,"Marks: ", self.marks)
    
    @staticmethod
    def disc():    
        print("Number of students: ", Student.count)

if __name__=="__main__":
    s1=Student("Pratham", 29)
    s2=Student("Vishnu", 30)
    s3=Student("Sathwik",45)
    Student.disc()
    s1.disp()
