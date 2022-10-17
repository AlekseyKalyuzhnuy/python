# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

data = list(map(str,input().split()))
print(data)
res = list(filter(lambda x: 'абв' not in x, data)) 
res = " ".join(res) 
print(res)
