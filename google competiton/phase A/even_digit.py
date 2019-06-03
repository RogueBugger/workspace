
def calcAns(n):
    minMinus,minPlus = 0, 0
    f = 1
    x = []
    n1 = ""
    for i in str(n):
        if int(i) % 2 != 0 and f != 0:
            x.append(str(int(i)-1))
            f = 0
        elif f == 0:
            x.append(str(8))
        else:
            x.append(str(i))
    minMinus = n1.join(x)
    x = []
    nx = ""
    n1 = list(map(int, str(n)))
    if n1[0] != 9:
        for i in str(n):
            if int(i) % 2 != 0 and int(i) != 9:
                x.append(str(int(i)+1))
                for i in range(n1.index(int(i)),len(n1)-1):
                    x.append(str(0))
                minPlus = nx.join(x)
                return abs(int(minPlus)-n), abs(int(minMinus)-n)
            elif int(i) != 9:
                    x.append(str(i)) 
    n1 = list(map(int, str(n)))
    nx = ""    
    if  n1[0] == 9 or (len(n1[n1.index(9)::-1]) - 1) == n1.count(8):
        n1 = [str(0) for _ in range(len(n1))]
        n1[0] = str(2)
        n1.append(str(0))
        minPlus = nx.join(n1)
        return abs(int(minPlus)-n), abs(int(minMinus)-n)
    n1 = list(map(int, str(n)))
    pos = n1.index(9)
    nx = ""
    pos = n1.index(9)
    print('passed here')
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
    n1 = [str(i) for i in n1]
    minPlus = nx.join(n1)  
    return abs(int(minPlus)-n), abs(int(minMinus)-n)
    

T = int(input())
for t in range(1, T+1):
    N = int(input())
    flag = 0
    for n in str(N):
        if int(n) % 2 != 0:
            flag = 1 
            break
    print("Case #{}: {}".format(t, min(calcAns(N))) )if flag == 1 else print("Case #{}: {}".format(t, 0))
            
