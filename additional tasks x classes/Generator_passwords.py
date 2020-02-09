import random

Numbers = ["0","1","2","3","4","5","6","7","8","9",]
Big_Letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
Small_Letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

print("Сколько цифр в пароле должно быть:")
numbers = int(input())

print("Сколько больших букв в пароле должно быть:")
b_letters = int(input())

print("Сколько маленьких букв в пароле должно быть:")
s_letters = int(input())

password = ""
pass_1 = ""
pass_2 = ""
pass_3 = ""

pass_m = []

for i in range(0,numbers,1):
    a = random.choice(Numbers)
    pass_1 = pass_1 + a
    pass_m.append(a)

for i in range(0,b_letters,1):
    b = random.choice(Big_Letters)
    pass_2 = pass_2 + b
    pass_m.append(b)
    
for i in range(0,s_letters,1):
    c = random.choice(Small_Letters)
    pass_3 = pass_3 + c
    pass_m.append(c)

password = pass_1 + pass_2 + pass_3

print("Пароль: " + password)
print("Перемешать? Y/N")
Mix = input()

if Mix == "Y":
    password = ""
    for i in range(0,len(pass_m),1):
        d = random.choice(pass_m)
        password = password + d
        pass_m.remove(d)
    print("Пароль: " + password)
else:
    print("Пароль: " + password)
