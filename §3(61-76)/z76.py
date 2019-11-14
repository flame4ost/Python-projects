from math import *
k = int(input("Введите текущую координату фигуры(вертикаль): "))
l = int(input("Введите текущую координату фигуры(горизонталь): "))
m = int(input("Введите координату для хода(вертикаль): "))
n = int(input("Введите координату для хода(горизонталь): "))
#if (k==m) and (k==m): print("Фигура может сделать ход")
#else: print("Фигура НЕ может сделать ход")
if (k==m) or (l==n):
   print('ЛАДЬЯ может сделать ход')
else:
    print('ЛАДЬЯ не может сделать ход')
if abs(k-m) == abs(l-n):
   print('слон')
if abs(k-m)==1 or abs(l-n)==1:
   print('король')
if abs(k-m) == abs(l-n) or k == m or l == n:
   print('ферзь')
if ((abs(abs(k-m)-2)<0.5) and (abs(abs(l-n)-1)<0.5)
    or (abs(abs(k-m)-1)<0.5) and (abs(abs(l-n)-2.0)<0.5)):
    print('конь')
