def  isprime(d):
    import math
 
    def is_prime(i):
        m = min(i, int(math.sqrt(n)))
        l = range(2, m)
        r = map(lambda x: i % x == 0, l)
        return not any(r)
 
    n = 100
    ls = range(2, n)
    ls2 = list(filter(is_prime, ls))
    print(ls2)
    # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
if __name__ == '__main__':
    d=int(input())
    isprime(d)
