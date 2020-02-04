import math
class Romb(object):
    def pi_Romb(self, dl_rebr):
        return (dl_rebr * 4)
    def pl_Romb(self, dl_rebr, dl_vis):
        return (dl_rebr * dl_vis)
 
class Pryamougolnik(object):
    def pi_Pryamougolnik(self, rebr_a, rebr_b):
        return float(rebr_a + rebr_b) * 2
    def pl_Pryamougolnik(self, rebr_a, rebr_b):
        return float(rebr_a + rebr_b)
 
class Ellipse(object):
    def pi_Ellipse(self, dl_rebr_a, dl_rebr_b):
        pi = float(3.14)
        return 4 * ((pi * dl_rebr_a * dl_rebr_b + (dl_rebr_a - dl_rebr_b) ** 2)/ (dl_rebr_a + dl_rebr_b))
    def pl_Ellipse(self, dl_rebr_a, dl_rebr_b):
        pi = float(3.14)
        return pi * dl_rebr_a * dl_rebr_b
 
while True:
    print('1: Ромб')
    print('2: Прямоугольник')
    print('3: Эллипс')
    vibor_fig = input('Выберите фигуру: ')
    if vibor_fig == '1':
        print('1: Периметр ромба')
        print('2: Площадь ромба')
        vibor_fun = input('Выберите решение: ')
        if vibor_fun == '1':
            p = Romb()
            print(p.pi_Romb(dl_rebr=float(input('Введите длину стороны: '))))
        elif vibor_fun == '2':
            p = Romb()
            print(p.pl_Romb(dl_rebr=float(input('Введите длину стороны: ')), dl_vis=float(input('Введите высоту стороны: '))))
 
    if vibor_fig == '2':
        print('1: Периметр прямоугольника')
        print('2: Площадь прямоугольника')
        vibor_fun = input('Выберите решение: ')
        if vibor_fun == '1':
            p = Pryamougolnik()
            print(p.pi_Pryamougolnik(rebr_a=float(input('Введите первую сторону: ')), rebr_b = float(input('Введите вторую сторону: '))))
        if vibor_fun == '2':
            p = Pryamougolnik()
            print(p.pl_Pryamougolnik(rebr_a=float(input('Введите сторону: ')), rebr_b = float(input('Введите высоту прямоугольника: '))))
 
    if vibor_fig == '3':
        print('1: Периметр эллипса')
        print('2: Площадь эллипса')
        vibor_fun = input('Выберите решение: ')
        if vibor_fun == '1':
            p = Ellipse()
            print(p.pi_Ellipse(dl_rebr_a=float(input('Введите длину стороны: ')), dl_rebr_b=float(input('Введите длину стороны: '))))
        if vibor_fun == '2':
            p = Ellipse()
            print(p.pl_Ellipse(dl_rebr_a=float(input('Введите длину стороны: ')), dl_rebr_b=float(input('Введите высоту: '))))
 
    print('Повторим?')
    print('1: Да')
    print('2: Нет')
    vop = int(input())
    if vop == 1:
        continue
    elif vop == 2:
        print('')
        break
