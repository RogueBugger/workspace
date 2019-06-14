
T = int(input())
for y in range(1, T+1):
    l , l1 = map(int, input().split())
    p = [str(input()) for _ in range(l1)]
    p = sorted(p, key = len)
    k = p.copy()
    for i in p:
        f = 0
        for j in p:
            if i[0:len(i)] == j[0:len(i)]  and len(i) != len(j) :
                if j in k:
                    k.remove(j)
    tm = 0
    com = 0
    for i in k:
        if len(i) == l:
            tm +=1
        else:
            com += pow(2, l - len(i))
    ans = pow(2, l) - com - tm
    print("Case #{}: {}".format(y, ans))






