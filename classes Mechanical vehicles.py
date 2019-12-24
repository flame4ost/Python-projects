class MechanicalVehicle:
    def __init__(self, l, w, h, c):
        self.length = l
        self.width = w
        self.height = h
        self.color = c

    def Ride(self):
        print("Move")

    def PrintInfo(self):
        print("\nSize: " + str(self.length) + "x" + str(self.width) + "x" + str(self.height))
        print("Color: " + self.color)

    def SetLength(self, l):
        self.length = l
    def SetWidth(self, w):
        self.width = w
    def SetHeight(self, h):
        self.height = h
    def SetColor(self, c):
        self.color = c    
        

class Car(MechanicalVehicle):
    
    def __init__(self, l, w, h, c, m, mp):
        MechanicalVehicle.__init__(self, l, w, h, c)
        self.model = m
        self.powerOfMotor = mp
        
    def Ride(self):
        print("\nStart engine")
        print("\Shiftt gear")
        print("Push gas pedal\n")
    def SetModel(self, m):
        self.model = m   
    def SetPower(self, mp):
        self.powerOfMotor = mp
    def PrintInfo(self):
        print("\nSize: " + str(self.length) + "x" + str(self.width) + "x" + str(self.height))
        print("Color: " + self.color)
        print("model: " + self.model)
        print("powerOfMotor: " + self.powerOfMotor)

class ElecticCar(Car):
    
    def __init__(self, l, w, h, c, m, mp, cb):
        Car.__init__(self, l, w, h, c, m, mp)
        self.model = m
        self.capacityOfBattery = cb
        self.powerOfMotor = mp
        
    def Ride(self):
        print("\nTurn on engine")
        print("Push pedal\n")
    def SetModel(self, m):
        self.model = m 
    def SetPower(self, mp):
        self.powerOfMotor = mp        
    def SetCapacity(self, cb):
        self.capacityOfBattery = cb
    def PrintInfo(self):
        print("\nSize: " + str(self.length) + "x" + str(self.width) + "x" + str(self.height))
        print("Color: " + self.color)
        print("model: " + self.model)
        print("powerOfMotor: " + self.powerOfMotor)
        print("capacityOfBattery: " + self.capacityOfBattery)

class Bus(MechanicalVehicle):
    def __init__(self, l, w, h, c, m, cw):
        MechanicalVehicle.__init__(self, l, w, h, c)
        self.model = m
        self.countOfSits = cs

    def Ride(self):
        print("\nHold steering wheel")
        print("Push pedals\n")
    def SetModel(self, m):
        self.model = m   
    def SetCountofSits(self, cs):
        self.countOfSits = cw
    def PrintInfo(self):
        print("\nSize: " + str(self.length) + "x" + str(self.width) + "x" + str(self.height))
        print("Color: " + self.color)
        print("model: " + self.model)
        print("countOfSits: " + self.countOfWheels)


class Minibus(Bus):
    def __init__(self, l, w, h, c, m, cs, mp):
        Bus.__init__(self, l, w, h, c, m, cs)
        self.powerOfMotor = mp

    def Ride(self):
        print("Hold steering wheel")
        print("Start engine")
        print("Push gas pedal\n")
    def SetModel(self, m):
        self.model = m   
    def SetPower(self, mp):
        self.powerOfMotor = mp   
    def SetCountofSits(self, cs):
        self.countOfSits = cs
    def PrintInfo(self):
        print("\nSize: " + str(self.length) + "x" + str(self.width) + "x" + str(self.height))
        print("Color: " + self.color)
        print("model: " + self.model)
        print("powerOfMotor: " + self.powerOfMotor)
        print("countOfSits: " + self.countOfSits)

isWorking = 1        
obj = 0
a = 0
while isWorking == 1:
    print("")
    print('1. Create Car')
    print('2. Create ElecticCar')
    print('3. Create Bus')
    print('4. Create MiniBus')
    print('5. Show info')
    print('6. Ride')
    print('7. Destroy object')
    print('0. Exit')
    print("")
    a = int(input('Enter action: '))

    if a == 1:
        l = input("Write length: ")
        w = input("Write width: ")
        h = input("Write height: ")
        c = input("Write color: ")
        m = input("Write model: ")
        mp = input("Write power of motor: ")
        obj = Car(l, w, h, c, m, mp)

    if a == 2:
        l = input("Write length: ")
        w = input("Write width: ")
        h = input("Write height: ")
        c = input("Write color: ")
        m = input("Write model: ")
        mp = input("Write power of motor: ")
        cb = input("Write power of capacity of battery: ")
        obj = ElecticCar(l, w, h, c, m, mp, cb)
        
    if a == 3:
        l = input("Write length: ")
        w = input("Write width: ")
        h = input("Write height: ")
        c = input("Write color: ")
        m = input("Write model: ")
        cw = input("Write countOfSits: ")
        obj = Bus(l, w, h, c, m, cs)
                   
    if a == 4:
        l = input("Write length: ")
        w = input("Write width: ")
        h = input("Write height: ")
        c = input("Write color: ")
        m = input("Write model: ")
        cw = input("Write countOfSits: ")
        mp = input("Write powerOfMotor: ")
        obj = MiniBus(l, w, h, c, m, cs, mp)
        
    if a == 5:
        if a != 0:
            obj.PrintInfo()  
    if a == 6:
        if a != 0:
            obj.Ride()
        
    if a == 7:
        obj = 0
        
    if a == 0:
        isWorking = 0
