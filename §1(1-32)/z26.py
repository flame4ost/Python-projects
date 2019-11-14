def area():
  r = 13.7
  radian=float(input("Введите число радиан дуги:"))
  if radian <= 0:
    print("Неверный ввод")
  else:
    square = radian/2 * (r*r)
    print(square)
      
if __name__ == '__main__':
  area()
