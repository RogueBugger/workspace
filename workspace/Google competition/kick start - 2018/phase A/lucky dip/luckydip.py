
def calcAns(N, vi, redip):
    if redip is 0:
        E = sum(vi) / N
    elif redip is 1:
        E = 










if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        N, redip = int(input()), int(input())
        vi = [int(input()) for _ in range(N)]
        print(calcAns(N, vi, redip))