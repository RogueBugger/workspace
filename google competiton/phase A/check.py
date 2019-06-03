
n = 2018
nj = ""
f = 1
x = []
'''for i in str(n):
    if int(i) % 2 != 0 and f != 0:
        x.append(str(int(i)-1))
        f = 0
    elif f == 0:
        x.append(str(8))
    else:
        x.append(str(i))
'''
n1 = list(map(int, str(n)))
for i in str(n):
    if int(i) % 2 != 0  and int(i) != 9 and str(n)[0] != 9:
        x.append(str(int(i)+1))
        for i in range(n1.index(int(i)),len(n1)-1):
            x.append(str(0))
        break
    else:
            x.append(str(i))

'''
n1 = list(map(int, str(n)))
if  n1[0] == 9 or (len(n1[n1.index(9)::-1]) - 1) == n1.count(8):
    n1 = [str(0) for _ in range(len(n1))]
    n1[0] = str(2)
    n1.append(str(0))'''
'''    
n1 = list(map(int, str(n)))


pos = n1.index(9)
if n1[pos-1] != 8:
    n1[pos - 1] = n1[pos - 1] + 2
    for i in range(pos, len(n1)):
        n1[i] = 0
else:
    while True:
        if n1[pos - 1] == 8:
            pos -=1
            continue 
        break
    n1[pos - 1] = n1[pos - 1] + 2
    for i in range(pos, len(n1)):
        n1[i] = 0
n1 = [str(i) for i in n1]'''
print(nj.join(x))













'''n1 = list(map(int, str(n)))
    for i in str(n):
        if int(i) % 2 != 0  and int(i) != 9 and str(n)[0] != 9 and 9 not in n1:
            x.append(str(int(i)+1))
            for i in range(n1.index(int(i))+1,len(str(n))):
                x.append(str(0))
            minPlus = nx.join(x)
            return int(minPlus), int(minMinus)
        else:
            x.append(str(i))'''