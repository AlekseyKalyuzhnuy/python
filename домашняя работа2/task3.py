
import random
n=int(input('Введите число n:'))
result=[]
elem=[random.randint(-n, n) for i in range(n)]
result.append(elem)
print(result[0])

print(random.shuffle(result))

data=open('file.txt', 'a')
data.writelines(str (result))
data.close()
