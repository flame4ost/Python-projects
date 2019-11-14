n = int(input())
suffix = ("год" if 11 <= n <= 19 or n % 10 == 1 else
          "года" if 2 <= n % 10 <= 4 else
          "лет")
print(f"{n} {suffix}")
