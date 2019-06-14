from itertools import product, combinations

T = int(input())
for y in range(1, T+1):
    le = int(input())
    N = list(map(int, input().split()))
    n = [str(i) for i in range(1, len(N)+1)]
    co = 0
    for i in list(combinations(n, 3)):
        li = list(map(int, i))
        li = [x - 1 for x in li]
        if li[0] < li[1] < li[2]:
            if int(N[li[0]]) * int(N[li[1]]) == int(N[li[2]]) or int(N[li[1]]) * int(N[li[2]]) == int(N[li[0]]) or int(N[li[0]]) * int(N[li[2]]) == int(N[li[1]]):
                co += 1

    print("Case #{}: {}".format(y, co))



            
