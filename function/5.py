# 1. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный. 
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Добавьте возможность использования скобок, меняющих приоритет операций.
# Пример: 1+2*3 => 7; (1+2)*3 => 9;

my_text = '1-2*3*4*2+8/4+9-3+7'
my_list = list(my_text)
print(my_list)

my_list1 = eval(my_text)
print(my_list1)

i = 1

while '*' in my_list or '/' in my_list:
    if my_list[i] == '*':
        my_list[i-1] = int(my_list[i-1]) * int(my_list[i+1])
        del my_list[i+1]
        del my_list[i]
    elif my_list[i] == '/':
        my_list[i-1] = int(my_list[i-1]) / int(my_list[i+1])
        del my_list[i+1]
        del my_list[i]
    else: i += 1

i = 1

while '+' in my_list or '-' in my_list:
    if my_list[i] == '+':
        my_list[i-1] = int(my_list[i-1] + int(my_list[i+1]))
        del my_list[i+1]
        del my_list[i]
    elif my_list[i] =='-':
        my_list[i-1] = int(my_list[i-1]) - int(my_list[i+1])
        del my_list[i+1]
        del my_list[i]
    else: i += 1

print(my_list)


