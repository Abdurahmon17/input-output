a1 = 1
b1 = 1
c1 = 5
a2 = 2
b2 = -1
c2 = 4
d = a1 * b2 - a2 * b1
dx = c1 * b2 - c2 * b1
dy = a1 * c2 - a2 * c1
x = dx / d
y = dy / d
print(int(x), round(y))

