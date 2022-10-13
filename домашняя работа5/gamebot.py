# Создайте программу для игры с конфетами человек против бота
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
    
    if num>28: s=28 #условия чтобы бот делал ход в пределах остатка конфет и не более 28
    else: s=num

    if k==0 :
       k=random.randint(1,s)
       print(f'ход компьютера: {k}')
       num = num-k
       if num==0:
        print("Победил компьютер")
        break
       else: 
        print(f'остаток конфет на столе {num}')
        n=0
     
       
    
