number = 324
first = number // 100
second = (number // 10) % 10
third = number % 10

print(str(first) + str(third) + str(second))