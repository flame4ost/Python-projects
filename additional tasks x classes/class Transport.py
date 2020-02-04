from __future__ import unicode_literals

class Vehicle(object):
    def __init__(self, speed, max_speed):
        self.speed = speed
        self.max_speed = max_speed
        print('Было создано транспортное средство')

    def accelerate(self,x):
        self.speed = self.speed + x
        if self.speed > self.max_speed:
            self.speed = self.max_speed

    def brake(self,x):
        self.speed = self.speed - x
        if self.speed < 0:
            self.speed = 0

    def print_status(self):
        print('Скорость транспортного средства равна {0} км/ч'.format(
            self.speed))


class Motorcycle(Vehicle):
    def __init__(self, speed, max_speed):
        Vehicle.__init__(self, speed, max_speed)
        # Дополнительные поля
        self._front_tire_width = 95
        self._rear_tire_width = 95

    def set_tires_width(self, front, rear):
        self._front_tire_width = front
        self._rear_tire_width = rear
        print('На мотоцикл были установлены новые шины')

    def print_tire_info(self):
        print('Ширина передней шины {0} мм'.format(self._front_tire_width))
        print('Ширина задней шины {0} мм'.format(self._rear_tire_width))


class Automobile(Vehicle):
    def __init__(self, speed, max_speed):
        Vehicle.__init__(self, speed, max_speed)
        # Дополнительные поля
        self._gear = 0
        self._color = 'синий'

    def set_gear(self, gear):
        self._gear = gear

    def print_status(self):
        Vehicle.print_status(self)
        print('Автомобиль переключен на скорость № {0}'.format(self._gear))
        print('Автомобиль покрашен в {0} цвет'.format(self._color))

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

print('>>> m = Motorcycle(40, 120)')
m = Motorcycle(40, 120)
print('>>> m.print_status()')
m.print_status()
print('>>> m.set_tires_width(90, 100)')
m.set_tires_width(90, 100)
print('>>> m.print_tire_info()')
m.print_tire_info()

print('\n\n>>> a = Automobile(0, 150)')
a = Automobile(0, 150)
print('>>> a.accelerate(40)')
a.accelerate(40)
print('>>> a.set_gear(2)')
a.set_gear(2)
print('>>> a.print_status()')
a.print_status()
print(">>> a.set_color('красный')")
a.set_color('красный')
print('>>> color = a.get_color()')
color = a.get_color()
print(color)
