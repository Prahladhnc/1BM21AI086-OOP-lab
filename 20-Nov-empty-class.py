class Student:
    pass
class Marks:
    pass

stud1=Student()
stud2=Student()

mark1=Marks()
mark2=Marks()
print("Type of stud1",type(stud1))
x=isinstance(stud1, Student)

y=isinstance(mark1, Marks)
print("Is stud1 instance of class Student?", x)

print("\nType of mark1",type(mark1))
print("Is mark1 instance of class Marks", y)
