## Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ 
# выведите на экран их сумму

is_OK = True
while is_OK:
    try:
      n = input('Введите число: ')
      n = float(n)
      n = int(n)
      is_OK = False
    except ValueError():
      print('вводить нужно число')

lst = []
for i in range(1,n+1):
    s = (1+1/i) ** i
    s = round(s)
    lst.append(s)
print(f'полученная сумма последовательности {lst} =', sum(lst))

