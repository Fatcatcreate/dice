fun=input('method?')
numdice=int(input("how mnay dice"))
l=[]
r=0
z=0
j=0
def repeat(x):
  for i in range (x):
    return i

for i in range (numdice):
  l.append(int(input('sides?')))

for i in l:
  suml=0
  suml=i//2+0.5+suml
  print(suml)
  j=j+suml
print(j)
for i in fun:
  if i == D:
    c=fun.index('D')
    z=fun[c+1]  

for i in l:
  k=[]
  b=[]
  for i in range (len(l)):
    p=repeat(i)
    k.append(p)
    k.sort()
    q=len(k)
    k.remove([z:q])
    b.append(k.sum())
  
d=sum(b)
avg=d/len(b)
