a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

temp = b
b = c
c = a
a = temp


print(a, b, c)