number = 324 #243
first = number // 100
second = (number // 10) % 10
third = number % 10

print(str(second) + str(third) + str(first))