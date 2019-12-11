s = str(input("Input string: "))

n = len(s)

ss = list(s)

i = 0
k = 0
f = 0

for i in range(n):
    if ss[i] == "a" and ss[i + 1] == "b" and ss[i + 2] == "c":
        k = k + 1
    if ss[i] == "a" and ss[i + 1] == "b" and ss[i + 2] == "a":
        f = f + 1
    i = i + 1
print("Count abc: " + str(k))
print("Count aba: " + str(f))
