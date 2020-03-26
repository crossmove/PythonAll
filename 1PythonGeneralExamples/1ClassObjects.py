'''
Python is object Oriented Lang, it posses following
1. Encapuslation
2. Data hiding and abstraction
3. Inheritance
4. Polymorphism(overloading/overridng)
5. Dynamic binding

Class Variable: A variable that is mutally shared by all  instance of a class. Works like static
variable in C#. Net. 

Instance Variable or Data Member

Instatatiation: Creation of an instance of a calss. 
Object
'''

class Student:
    'This is a Student Class, documenation string: Summmary in C#'
    #Variables decalred outside __init__() are called class variables. Acts as static variable in C#
    studentCount = 0

#the init method is mandatory to be called to declare the class data members(instance members)
    def __init__(self, name, id):   #Class constructor
        self.name = name  #instance/data member
        self.id = id      #instance/data member

        Student.studentCount += 1   #Class variables should be accessed through ClassName.ClassVariable

    #In Python, it is mandatory to write self as an arugment to all class methods. While 
    # calling this function, the self is not passed as an argument.
    def displayCount(self):         
        print("Total Student", Student.studentCount)
    
    def displayStudent(self):
        print('Name',self.name,'Id',self.id)
    
    def inputFunction(self):
        self.place = input('Enter the place')  #Read input from command line and assingn to self.place


if __name__ == "__main__":
    studentPradeep  =  Student('pradeep', 10)
    studentSvar  =  Student('Svar', 20)

    studentPradeep.displayStudent()
    studentSvar.displayStudent()

    studentPradeep.displayCount()   #This methods returns 2
    studentSvar.displayCount()      # this also return 2


'''Output
('Name', 'pradeep', 'Id', 10)
('Name', 'Svar', 'Id', 20)
('Total Student', 2)
('Total Student', 2)
'''

