# найти наименьшее общее кратное

a, b= 6, 8
i = max (a ,b)
while not (i%a==0 and i%b==0): # i%a!=0 or i%b!=0
    i += max(a, b)
print(i)



