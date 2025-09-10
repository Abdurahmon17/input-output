a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

temp = a
a = c
c = b
b = temp

print(a, b, c)