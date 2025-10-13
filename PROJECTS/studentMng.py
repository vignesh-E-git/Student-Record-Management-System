from abc import ABC,abstractmethod

class Person(ABC):
    @abstractmethod
    def display_info(self): # ABSTRACTION CONCEPT
        pass
    
class Student(Person):
    def __init__(self,name,std,mark):
        self.name = name
        self.std = std
        self.__mark = mark # private -> ENCAPTULATION
    def display_info(self):
        print(f'NAME : {self.name}\nSTANDARD : {self.std}')
    def get_mark(self):
        print(f'MARK : {self.__mark}')
    def _set_mark(self,mark): # student can't change their mark.
        self.__mark = mark
        
class Teacher(Person): # -> INHERITANCE
    def __init__(self,name,subject,number):
        self.name=name
        self.subject = subject
        self.__number = number # private
    def get_number(self):
        print(f'NUMBER : {self.__number}')
    def display_info(self):
        print(f'NAME : {self.name}\nSUBJECT : {self.subject}')
    def set_mark(self,mark,studentNO):
        studentNO._set_mark(mark)
        
def Display_info(role): # POLYMORPHISM FUNCTION
    return role.display_info()
        
student1 = Student("vignesh",12,94)
student2 = Student('akash',12,88)
teacher1 = Teacher("lewin","physics",9876543210)

Display_info(student1)
Display_info(teacher1)

student1.get_mark()
teacher1.get_number()

try:
    student1.set_mark(100)
except AttributeError:
    print(f'student cannot modify their mark.')
    
teacher1.set_mark(89,student1)
teacher1.set_mark(99,student2)
student1.get_mark()
student2.get_mark()