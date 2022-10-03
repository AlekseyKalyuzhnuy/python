# программа принимает на ввод число N и выдает набор произведений чисел от 1 до N

def fact(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return res

n= input('Введите число n:')
result=[]
for i in range(1, int(n)+1):
    elem=[fact(i)]
    result.append(elem)
print(result)  







