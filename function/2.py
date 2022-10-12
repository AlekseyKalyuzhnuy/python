# использование filter

data = [x for x in range(10)]
res = list(filter(lambda x: not x%2, data))  # not %2 тоже самое x%2==0
print(res)