from collections import Counter
 
n = input().strip()
if n == n[::-1]:
    print("Palindrome")
if any(count == 3 for digit, count in Counter(n).most_common()):
    print("chislo soderzhit tri odinakovyh chisla!")
if len(set(n)) == len(n):
    print("Vse chetyre cifry razlichny!")
