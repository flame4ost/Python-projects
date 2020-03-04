class Human:
    name = 'a'
    surname = 'b'
    patronimic = 's'
    age = 0
    gender = 'm'
    counter = 0

    def setName(self, n):
        self.name = n
    def setSurname(self, s):
        self.surname = s
    def setPatron(self, p):
        self.patronimic = p
    def setAge(self, a):
        self.age = a
    def setGender(self, g):
        self.gender = g

    def getName(self):
        print ("Name: " + self.name)
    def getSurname(self):
        print("Surname: " + self.surname)
    def getPatron(self):
        print("Patronimic: " + self.patronimic)
    def getAge(self):
        int(self.age)
        print("Age: %.2f" % self.age)
    def getGender(self):
        print("Gender: " + self.gender)

    @staticmethod
    def init(self ):
        print("New Human")
        self.counter += 1
        Human.counter += 1
    def init(self, name, surname, patron):
        self.name = name
        self.surname = surname
        self.patronimic = patron
        print("Name: " + self.name)
        print("Surname: " + self.surname)
        print("Patronimic: " + self.patronimic)
    def init(self,name, surname, patron, age):
        self.name = name
        self.surname = surname
        self.patronimic = patron
        self.age = age
        print("Name: " + self.name)
        print("Surname: " + self.surname)
        print("Patronimic: " + self.patronimic)
        print("Age: .%2f" % self.age)
    def init(self, gender, name, surname, patron, age):
        self.name = name
        self.surname = surname
        self.patronimic = patron
        self.age = age
        print("Name: " + self.name)
        print("Surname: " + self.surname)
        print("Patronimic: " + self.patronimic)
        print("Age: %.2f" % self.age)
        self.gender = gender
        print("Gender: " + self.gender)
        
class Apartment:    
    def __init__(self, number, condition, storey, chambers):
        """
        number - номер квартиры
        condition - состояние кваритры
        storey  - номер этажа
        chambers - количество комнат
        """
        self.number = number
        self.storey = storey
        self.condition = condition
        self.chambers = chambers
        self.people = [] # жильцы этой квартиры
 
    def add(self, human):
        """
        Метод добавления жильца в квартиру
        """
        self.people.append(human)
    
 
    def __str__(self):
        res = "number: {}, codition: {}\n".format(self.number, self.condition)
        for h in self.people:
            res += str(h) + "\n"
        return res    
# добавить квартиры, реализовать метод add, __str__
class House:  
    """
    Это дом в котором живут люди
    """
    def __init__(self, number=1, address="BVD Shevchenka"):
        self.address = address
        self.number = number
        self.apart = []
        
    def add(self,apartment):
        self.apart.append(apartment)
        
    def __str__(self):
        res = "house number: {}, address: {}\nappartments: {}\n".format(self.number, self.address, len(self.apart))
        for h in self.apart:
            res += str(h) + "\n"
        return res

def dels():
    print("Destructing")


name = str(input("Enter Name: "))
surname = str(input("Enter Surname: "))
patronimic = str(input("Enter Patronimic: "))
age = int(input("Enter Age: "))
gender = str(input("Enter Gender:"))

cl = Human()

print("set and get Name")
cl.setName(name)
cl.getName()
print("set and get Surname")
cl.setSurname(surname)
cl.getSurname()
print("set and get Patronimic")
cl.setPatron(patronimic)
cl.getPatron()
print("set and get Age")
cl.setAge(age)
cl.getAge()
print("set and get Gender")
cl.setGender(gender)
cl.getGender()
print("Total number of objects created: ", Human.counter )
