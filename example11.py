#   задать строку из набора чисел. В качества символа-разделителя используйте пробел
#   найти большее и меньшее число

#k="1 2 3 5 7 9 45"
#result = list(map(int, (k.split())))
#print(max(result), min(result))

# второе решение
nums = '5 67 3 4 89 345 2 7 45'
my_list = [int(num) for num in nums.split()]
print(min(my_list), max(my_list))