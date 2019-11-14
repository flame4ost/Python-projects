import math
phi = int(input("phi = "))
hours, minutes = divmod(phi, 30)
minutes *= 12
print(f"{hours} часа {minutes} минут")
