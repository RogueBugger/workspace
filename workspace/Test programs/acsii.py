import random
ls=[]
#producing alphabets 
for _ in range(100):
    a=chr(random.randint(97,123))
    if a not in ls:
        print(a)
        ls.append(a)
print(len(ls))
