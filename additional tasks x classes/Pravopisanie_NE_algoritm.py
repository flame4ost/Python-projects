import time
Clovo = ""
Chast = ""
Nomer = 0
print("Данная программа поможет вам проверить написание НЕ (слитно/раздельно)!")
print()
def Start(Clovo,Chast,Nomer):
    try:
        Clovo = str(input("Bведите предложение с затрудняющим написанием НЕ: "))
        Ypotreblenie(Clovo,Chast,Nomer)
    except:
        print("Ошибка! Попробуй ещё раз!")
        Start(Clovo,Chast,Nomer)
def Ypotreblenie(Clovo,Chast,Nomer):
    try:
        Nomer = 1
        Ypotr = str(input(str(Nomer) + ".Это слово употребляется без НЕ? (Да/Нет): "))
        if (Ypotr == "Да"):
            Chast_rechi(Clovo,Chast,Nomer)
        elif (Ypotr == "Нет"):
            print(Clovo)
            print("Пиши слитно! НЕ - часть корня или приставка.")
        else:
            print("Ошибка! Попробуй ещё раз! Ответь \"Да\" или \"Нет\".")
            Ypotreblenie(Clovo,Chast,Nomer)
    except:
        print("Ошибка! Попробуй ещё раз! Ответь \"Да\" или \"Нет\".")
        Ypotreblenie(Clovo,Chast,Nomer)
def Chast_rechi(Clovo,Chast,Nomer):
    try:
        Nomer = 2
        Chast = str(input(str(Nomer) + ".Какая это часть речи? (Пиши полностью): "))
        if (Chast == "Имя существительное"):
            Cych(Clovo,Chast,Nomer)
        elif (Chast == "Имя прилагательное"):
            Pril(Clovo,Chast,Nomer)
        elif (Chast == "Имя числительное"):
            Chisl(Clovo,Chast,Nomer)
        elif (Chast == "Местоимение"):
            Mect(Clovo,Chast,Nomer)
        elif (Chast == "Глагол"):
            Glag(Clovo,Chast,Nomer)
        elif (Chast == "Наречие"):
            Narech(Clovo,Chast,Nomer)
        elif (Chast == "Причастие"):
            Prich(Clovo,Chast,Nomer)
        elif (Chast == "Деепричастие"):
            Deeprich(Clovo,Chast,Nomer)
        else:
            print("Ошибка! Попробуй ещё раз! Ответь \"Имя существительное\", \"Имя прилагательное\", \"Имя числительное\", \"Местоимение\", \"Глагол\", \"Наречие\", \"Причастие\" или \"Деепричастие\".")
            Chast_rechi(Clovo,Chast,Nomer)
    except:
        print("Ошибка! Попробуй ещё раз! Ответь \"Имя существительное\", \"Имя прилагательное\", \"Имя числительное\", \"Местоимение\", \"Глагол\", \"Наречие\", \"Причастие\" или \"Деепричастие\".")
        Chast_rechi(Clovo,Chast,Nomer)
def Cych(Clovo,Chast,Nomer):
    Antonim(Clovo,Chast,Nomer)
    
def Pril(Clovo,Chast,Nomer):
    Crav_ctep(Clovo,Chast,Nomer)
    
def Chisl(Clovo,Chast,Nomer):
    print(Clovo)
    print("Пишу раздельно! НЕ - частица.")
    
def Mect(Clovo,Chast,Nomer):
    Opred_Mect(Clovo,Chast,Nomer)
def Glag(Clovo,Chast,Nomer):
    nedo(Clovo,Chast,Nomer)
def Narech(Clovo,Chast,Nomer):
    Crav_ctep(Clovo,Chast,Nomer)
def Prich(Clovo,Chast,Nomer):
    Antonim(Clovo,Chast,Nomer)
def Deeprich(Clovo,Chast,Nomer):
    nedo(Clovo,Chast,Nomer)
def Antonim(Clovo,Chast,Nomer):
    try:
        Nomer += 1
        print(Clovo)
        ant = str(input(str(Nomer) + ".В предложении есть антонимы/текстовые антонимы? (Да/Нет): "))
        if (ant == "Да"):
            print(Clovo)
            print("Пиши раздельно! НЕ - частица.")
        elif (ant == "Нет"):
            if (Chast == "Причастие"):
                Zavicemoe_clovo(Clovo,Chast,Nomer)
            else:
                Vovce(Clovo,Chast,Nomer)
        else:
            Nomer -= 1
            print("Ошибка! Попробуй ещё раз! Ответь \"Да\" или \"Нет\".")
            Antonim(Clovo,Chast,Nomer)
    except:
        Nomer -= 1
        print("Ошибка! Попробуй ещё раз! Ответь \"Да\" или \"Нет\".")
        Antonim(Clovo,Chast,Nomer)
def Vovce(Clovo,Chast,Nomer):
    try:
        Nomer += 1
        vov = str(input(str(Nomer) + ".В предложении есть слова: вовсе не, далеко не, отнюдь не, совсем не (=отнюдь не), ничуть не, никому не, ничем не, нисколько не и т.д.? (Да/Нет): "))
        if (vov == "Да"):
            print(Clovo)
            print("Пиши раздельно! НЕ - частица.")
        elif (vov == "Нет"):
            if (Chast == "Причастие"):
                Prich_Mui(Clovo,Chast,Nomer)
            else:
                Cinonim(Clovo,Chast,Nomer)
        else:
            Nomer -= 1
            print("Ошибка! Попробуй ещё раз! Ответь \"Да\" или \"Нет\".")
            Vovce(Clovo,Chast,Nomer)
    except:
        Nomer -= 1
        print("Ошибка! Попробуй ещё раз! Ответь \"Да\" или \"Нет\".")
        Vovce(Clovo,Chast,Nomer)
def Cinonim(Clovo,Chast,Nomer):
    try:
        Nomer += 1
        cin = str(input(str(Nomer) + ".Можно заменить синонимом без НЕ? (Да/Нет): "))
        if (cin == "Да"):
            print(Clovo)
            print("Пиши слитно! НЕ - приставка.")
        elif (cin == "Нет"):
            print(Clovo)
            print("Пиши раздельно! НЕ - частица.")
        else:
            Nomer -= 1
            print("Ошибка! Попробуй ещё раз! Ответь \"Да\" или \"Нет\".")
            Cinonim(Clovo,Chast,Nomer)
    except:
        Nomer -= 1
        print("Ошибка! Попробуй ещё раз! Ответь \"Да\" или \"Нет\".")
        Cinonim(Clovo,Chast,Nomer)
def Crav_ctep(Clovo,Chast,Nomer):
    try:
        Nomer += 1
        crav = str(input(str(Nomer) + ".Слово в сравнительной степени? (Да/Нет): "))
        if (crav == "Да"):
            print(Clovo)
            print("Пиши раздельно! НЕ - частица.")
        elif (crav == "Нет"):
            if (Chast == "Имя прилагательное"):
                Antonim(Clovo,Chast,Nomer)
            elif (Chast == "Наречие"):
                O_e(Clovo,Chast,Nomer)
            else:
                Chast_rechi(Clovo,Chast,Nomer)
        else:
            Nomer -= 1
            print("Ошибка! Попробуй ещё раз! Ответь \"Да\" или \"Нет\".")
            Crav_ctep(Clovo,Chast,Nomer)
    except:
        Nomer -= 1
        print("Ошибка! Попробуй ещё раз! Ответь \"Да\" или \"Нет\".")
        Crav_ctep(Clovo,Chast,Nomer)
def O_e(Clovo,Chast,Nomer):
    try:
        Nomer += 1
        oe = str(input(str(Nomer) + ".Наречие заканчивается на \"-О\",\"-Е\"? (Да/Нет): "))
        if (oe == "Да"):
            Antonim(Clovo,Chast,Nomer)
        elif (oe == "Нет"):
            print(Clovo)
            print("Пиши раздельно! НЕ - частица.")
        else:
            Nomer -= 1
            print("Ошибка! Попробуй ещё раз! Ответь \"Да\" или \"Нет\".")
            O_e(Clovo,Chast,Nomer)
    except:
        Nomer -= 1
        print("Ошибка! Попробуй ещё раз! Ответь \"Да\" или \"Нет\".")
        O_e(Clovo,Chast,Nomer)
def nedo(Clovo,Chast,Nomer):
    try:
        Nomer += 1
        ne = str(input(str(Nomer) + ".В слове есть приставка НЕДО (ниже нормы)? (Да/Нет): "))
        if (ne == "Да"):
            print(Clovo)
            print("Пиши слитно! НЕ - часть приставки НЕДО.")
        elif (ne == "Нет"):
            print(Clovo)
            print("Пиши раздельно! НЕ - частица.")
        else:
            Nomer -= 1
            print("Ошибка! Попробуй ещё раз! Ответь \"Да\" или \"Нет\".")
            nedo(Clovo,Chast,Nomer)
    except:
        Nomer -= 1
        print("Ошибка! Попробуй ещё раз! Ответь \"Да\" или \"Нет\".")
        nedo(Clovo,Chast,Nomer)
def Opred_Mect(Clovo,Chast,Nomer):
    try:
        Nomer += 1
        opred = str(input(str(Nomer) + ".Это неопределённое/отрицательное местоимение? (Да/Нет): "))
        if (opred == "Да"):
            V3clova(Clovo,Chast,Nomer)
        elif (opred == "Нет"):
            print(Clovo)
            print("Пиши раздельно! НЕ - частица.")
        else:
            Nomer -= 1
            print("Ошибка! Попробуй ещё раз! Ответь \"Да\" или \"Нет\".")
            Opred_Mect(Clovo,Chast,Nomer)
    except:
        Nomer -= 1
        print("Ошибка! Попробуй ещё раз! Ответь \"Да\" или \"Нет\".")
        Opred_Mect(Clovo,Chast,Nomer)
def V3clova(Clovo,Chast,Nomer):
    try:
        Nomer += 1
        clova = str(input(str(Nomer) + ".Между НЕ/НИ и корнем есть предлог? (Да/Нет): "))
        if (clova == "Да"):
            print(Clovo)
            print("Пиши раздельно в 3 слова! НЕ/НИ - частица.")
        elif (clova == "Нет"):
            print(Clovo)
            print("Пиши слитно! НЕ/НИ - приставка.")
        else:
            Nomer -= 1
            print("Ошибка! Попробуй ещё раз! Ответь \"Да\" или \"Нет\".")
            V3clova(Clovo,Chast,Nomer)
    except:
        Nomer -= 1
        print("Ошибка! Попробуй ещё раз! Ответь \"Да\" или \"Нет\".")
        V3clova(Clovo,Chast,Nomer)
def Zavicemoe_clovo(Clovo,Chast,Nomer):
    try:
        Nomer += 1
        print(Clovo)
        zavicemoe = str(input(str(Nomer) + ".При причастии есть зависимые слова? (Да/Нет): "))
        if (zavicemoe == "Да"):
            print(Clovo)
            print("Пиши раздельно! НЕ - частица.")
        elif (zavicemoe == "Нет"):
            Kratkoe_prich(Clovo,Chast,Nomer)
        else:
            Nomer -= 1
            print("Ошибка! Попробуй ещё раз! Ответь \"Да\" или \"Нет\".")
            Zavicemoe_clovo(Clovo,Chast,Nomer)
    except:
        Nomer -= 1
        print("Ошибка! Попробуй ещё раз! Ответь \"Да\" или \"Нет\".")
        Zavicemoe_clovo(Clovo,Chast,Nomer)
def Kratkoe_prich(Clovo,Chast,Nomer):
    try:
        Nomer += 1
        kratkoe = str(input(str(Nomer) + ".Это краткое причастье? (Да/Нет): "))
        if (kratkoe == "Да"):
            print(Clovo)
            print("Пиши раздельно! НЕ - частица.")
        elif (kratkoe == "Нет"):
            Vovce(Clovo,Chast,Nomer)
        else:
            Nomer -= 1
            print("Ошибка! Попробуй ещё раз! Ответь \"Да\" или \"Нет\".")
            Kratkoe_prich(Clovo,Chast,Nomer)
    except:
        Nomer -= 1
        print("Ошибка! Попробуй ещё раз! Ответь \"Да\" или \"Нет\".")
        Kratkoe_prich(Clovo,Chast,Nomer)
def Prich_Mui(Clovo,Chast,Nomer):
    try:
        Nomer += 1
        print(Clovo)
        mui = str(input(str(Nomer) + ".У причастия на -мый есть зависимое слово в творительном падеже? (Да/Нет): "))
        if (mui == "Да"):
            print(Clovo)
            print("Пиши раздельно! НЕ - частица.")
        elif (mui == "Нет"):
            print(Clovo)
            print("Пиши слитно! НЕ - приставка.")
        else:
            Nomer -= 1
            print("Ошибка! Попробуй ещё раз! Ответь \"Да\" или \"Нет\".")
            Prich_Mui(Clovo,Chast,Nomer)
    except:
        Nomer -= 1
        print("Ошибка! Попробуй ещё раз! Ответь \"Да\" или \"Нет\".")
        Prich_Mui(Clovo,Chast,Nomer)
Start(Clovo,Chast,Nomer)


    
