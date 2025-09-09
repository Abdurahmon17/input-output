import math

s = int(input("S ni kiriting: "))
r = math.sqrt(s/round(math.pi, 3))
d = 2*r
l = 2*round(math.pi, 3)*r
print(round(d), round(l, 1))