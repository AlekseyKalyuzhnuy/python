# Создайте программу для игры с конфетами человек против бота c ителектом

import random
start = random.randint(1,2)
print(start) # случайный выбор порядкового номера для старта
n=0
k=0
num = 2021 # остаток конфет на столе
while num>0: 
    if n==0: 
      n=int(input('игрок №1, ваш ход: '))
      if n> 28: 
        print("по условию игры можно брать не более 28 конфет в один ход")
        n=0
        k=1
      elif n>num: 
        print("на столе нет столько конфет ") 
        n=0
        k=1
      elif n<num and n<29: 
        num = num-n
        print(f'остаток конфет на столе {num}')
        k=0
      elif n==num and n<29:
        print("победил игрок №1")
        break
    
    s=num//28
    print (s)
    if s<=1:
     g=num
    elif s % 2==0:
     s=s-1   
     g=num-1-28*s
     print(g)
    else:
     g=num-1-28*s
     print(g)

    if k==0 :
       print(f'ход компьютера: {g}')
       num = num-g
       if num==0:
        print("Победил компьютер")
        break
       else: 
        print(f'остаток конфет на столе {num}')
        n=0