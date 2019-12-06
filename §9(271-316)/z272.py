import sys
 
N = 50
 
def input_func(mas, sr):
    for i in range(0, N):
        print('Введите кол-во осадков в {} году.'.format(i + 1900))
        
        mas.append(float(input()))
 
        sr += mas[i]
 
def proc(mas, sr):
    for i in range(0, N):
        if mas[i] > sr:
            print('В {} кол-во осадков было на {} мл больше нормы.'.format(1900 + i + 1, mas[i] - sr))
        elif mas[i] < sr:
            print('В {} кол-во осадков было на {} мл меньше нормы.'.format(1900 + i + 1, -1 * (mas[i] - sr)))
        else:
            print('В {} кол-во осадков было в норме.'.format(1900 + i + 1))
 
def main():
    mas = []
    
    sr = 0
 
    input_func(mas, sr)
 
    print('Среднее кол-во осадков = {}.'.format(sr))
 
    proc(mas, sr)
 
    return 0
 
if __name__ == '__main__':
    sys.exit(main())
