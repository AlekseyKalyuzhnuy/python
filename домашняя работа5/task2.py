# Создайте программу для игры с конфетами человек против человека
import random
start = random.randint(1,2)
print(start)
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
      elif n<num and n<28: 
        num = num-n
        print(num)
        k=0

    if k==0 : 
       k=int(input('игрок №2, ваш ход: '))
       if k> 28: 
         print("по условию игры можно брать не более 28 конфет в один ход")
         k=0
       elif n>num: 
           print("на столе нет столько конфет ") 
           k=0
       elif k<num and k<28: 
           num = num-k
           print(num)
           n=0
     





