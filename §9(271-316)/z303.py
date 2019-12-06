import sys
 
def main():
    p = [0] * 101
    x = []
 
    for i in range(0, 200):
        x.append(float(input()))
 
        k = x[i] * 100 + 0.5
 
        p[int(k)] += 1
 
    for i in range(1, 101):
        print('p[{}]={} '.format(i, int(p[i]/2000)))
 
        if i % 10 == 0:
            print('\n')
 
    return 0
 
if __name__ == '__main__':
    sys.exit(main())
