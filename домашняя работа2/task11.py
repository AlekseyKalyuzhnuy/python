# программа принимает на ввод вещественное число и 
# выдает сумму его цифр (второй вариант решения
number = input("Введите число ") # принимаем на ввод число (как текст)
result=0 # создаем переменную для счетчика
for i in number: # пока переменная находится в диапазоне проверяем условие
    if i.isdigit(): # если символ в строке является цифрой, то...
      result=result+int(i)
print(f"сумма цифр введенного числа {number} равняется: {result} ")

