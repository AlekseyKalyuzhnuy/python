# программа принимает на ввод число N и выдает набор произведений чисел от 1 до N

n = input('Введите  число ')
while not n.isdigit():
    n = input('Введены некорректные данные, введите снова') # проверка на "дурака"
n = int(n)
result = list()
j = 1
for i in range(n):
    j=(i+1) * j
    result.append(j)
print(result)

