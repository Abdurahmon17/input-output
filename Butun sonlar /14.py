number = 324 #432
first = number // 100
second = (number // 10) % 10
third = number % 10

print(str(third) + str(first) + str(second))