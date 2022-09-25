# Array=[]
# for i in range(5):
#    z=int(input ("Введите число "))
#    Array.append(z)
#    maxnum=Array[0]
#    if Array[i] > maxnum:
#      maxnum=Array[i]

#print(Array)
   
#print(maxnum)


Array=[]
for i in range(5):
  z=int(input ("Введите число "))
  Array.append(z)
print(Array)

maxnum=Array[0]
for i in range(5):
   if Array[i] > maxnum: maxnum=Array[i]
   
print(maxnum)
