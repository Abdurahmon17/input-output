number = 324 #234
first = number // 100
second = (number // 10) % 10
third = number % 10

print(str(second) + str(first) + str(third))