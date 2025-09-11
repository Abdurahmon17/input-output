son = 324
a = (son // 10) % 10
a2 = son % 10

temp = a
a = a2
a2 = temp

print(a, a2)