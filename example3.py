num= input('Введите число: ')
count=0
not_num=0
for i in num:
    count += 1
    if i == "," or ".":
        not_num=1
    print(num[count])
if not_num==0: 
    print ("Нет")

