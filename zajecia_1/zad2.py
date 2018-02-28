a = [0,0,0]

max = 0

for i in range(3):

 a[i] = input('')

 if int(a[i])>int(max):
  max = a[i]
print(max)