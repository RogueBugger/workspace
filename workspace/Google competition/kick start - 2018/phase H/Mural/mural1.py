from math import ceil

T = int(input())
for k in range(1, T+1):
    N = int(input())
    va = input()
    n = [int(i) for i in va]
    clen = ceil(len(n) / 2)
    i = 0
    max = 0
    for _ in range(0, clen+1):
        max = sum(n[0:clen]) if max < sum(n[0:clen]) else max 
        n.pop(0)
    print("Case #{}: {}".format(k, max))




    