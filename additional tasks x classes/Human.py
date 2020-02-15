class Human:
    name = 'a'
    surname = 'b'
    patronimic = 's'
    age = 0
    gender = 'm'

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
        print("Age: .%2f" % self.age)
    def getGender(self):
        print("Gender: " + self.gender)

    @staticmethod
    def init():
        print("New Human")
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
        print("Age: .%2f" % self.age)
        self.gender = gender
        print("Gender: " + self.gender)


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