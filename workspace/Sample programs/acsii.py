import random
ls=[]
#producing alphabets 
for _ in range(100):
    a=chr(random.randint(97,123))
    if a not in ls:
        print(a)
        ls.append(a)
print(len(ls))
from math import factorial
r=3
fac=factorial(r*r)
li=[[] for _ in range(fac)]
#print(li)
nre=[]
co=0
for i in range(3):
    for j in range(3):
        for k in range(3):
            v=[i,j,k]
            nre.append(v)
            co+=1

print(nre)
print(co)
for i in range(97,123):
    print(chr(i))