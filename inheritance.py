#Inheritance( Kalıtım): Miras alma
#Peerson => name , lastname , age , eat() , run(), drink()
#Student(Person), Teacher(Person)
#Animal = Dog(Animal) , Cat(Animal) 

class Person():
    def __init__(self,fname,lname):
        self.firstName = fname
        self.lastName = lname
        print('Person Created')

    def whoAmI(self):
        print('I am a person')

    def eat(self):
        print('I am eating')

class Student(Person):
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        self.studentNumber = number
        print('Student Created')

    #ovvereide
    def whoAmI(self): #aynı isimli bir metod temel sınıftaki metodu ezer 
        print('I am a student')

    def sayHello(self):
        print('Hello i am e student')

class Teacher(Person):
    def __init__(self, fname, lname,branch):
        super().__init__(fname, lname)
        self.branch = branch
    
    def whoAmI(self):
        print(f'I am a {self.branch} teacher')


p1 = Person('Berfin', 'Çelik')
s1 = Student('Güler' ,'Çelik', 223)
t1 = Teacher('Soner','Çelik','Math')

print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName + ' ' + str(s1.studentNumber))

p1.whoAmI()
s1.whoAmI()
p1.eat()
s1.eat() 
s1.sayHello()
t1.whoAmI()