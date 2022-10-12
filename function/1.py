#  пример создания списка с клавиатуры (через пробел)
data = list(map(int, input().split()))
print(data)

res = filter(lambda x: not x%2, data)
res = list(map(lambda x: (x, x**2),res))
print(res)





