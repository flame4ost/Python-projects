import sys
 
N = 3
 
def main():
    flag = False
    arr = []
    
    for i in range(0, N):
        arr.append(float(input()))
 
        if i != 0:
            if (arr[i - 1] * arr[i - 1] > arr[i] * arr[i]) and (arr[i] < 0):
                flag = True
 
    if flag:
        summ = 0
        
        for i in range(0, N):
            summ += arr[i]
 
        print(summ)
    else:
        proizv = 1
        
        for i in range(0, N):
            proizv *= arr[i]
 
        print(proizv)
 
    return 0
 
if __name__ == '__main__':
    sys.exit(main())
