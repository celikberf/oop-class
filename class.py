#class

class Person:
    pass

    # class attributes
    address = 'no information'
    # constructor (yapıcı metod)

    def __init__(self, name , year): #attribusteslerın üzerine bunları aktarıcaz
        #object attributes
        self.name = name
        self.year = year

    #instance methods
    def intro(self):
        print('Hello There + I am ' + self.name)

    #instance methods
    def calculateAge(self):
        return 2024 - self.year


#object,(instance)

p1 = Person(name = 'berf', year = 1999)
p2 = Person(name = 'guler',year = 1973)

p1.intro()
p2.intro()

print(f"adım : {p1.name} yaşım : {p1.calculateAge()}")
print(f"adım : {p2.name} yaşım : {p2.calculateAge()}")



#accessing object attributes
# print(f"name1: {p1.name} year: {p1.year} adres: {p1.address}")
# print(f"name2: {p2.name} year: {p2.year} adres: {p2.address}")

