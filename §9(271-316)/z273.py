class Point:
    __slots__ = 'x', 'y', 'm'
    
    def __init__(self, x, y, m):
        self.x = x
        self.y = y
        self.m = m
        
 
ls = (
    Point(0, 0, 3),
    Point(0, 2, 3),
    Point(2, 0, 3),
    Point(2, 2, 3),
)
 
m_sum = sum(i.m for i in ls)
xc = sum(i.x * i.m for i in ls) / m_sum
yc = sum(i.y * i.m for i in ls) / m_sum
print(xc, yc)
