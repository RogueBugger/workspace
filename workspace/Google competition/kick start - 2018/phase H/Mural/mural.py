from math import ceil, floor

def calcAns(side, va):
    if len(va) % 2 == 0:
        left, right = va[0 : ceil(len(va) / 2)], va[ceil(len(va) / 2):]  
    else:
        left, right = va[0 : ceil(len(va) / 2)], va[floor(len(va) / 2):]

    co = 0
    se = 0
    while se != len(va) - 1:
        print(left[0], right[len(right) - 1])
        if left[0] < right[len(right) - 1] and (len(left) and len(right) != 1):
            co += int(right[0])
            right.pop(0)
            left.pop(0)
            se += 1
        elif left[0] > right[len(right) - 1] and (len(left) and len(right) != 1):
            co += int(left[len(left) - 1])
            left.pop(len(left) - 1)
            right.pop(len(right) - 1)
            se += 1
        elif left[0] == right[len(right) - 1] and (len(left) and len(right)) != 1:
            if side == 'left':
                co += int(right[0])
                right.pop(0)
                left.pop(0)
                se += 1
            elif side == 'right':
                co += int(left[len(left) - 1])
                left.pop(len(left) - 1)
                right.pop(len(right) - 1)
                se += 1
        else:
            co += int(max(left[0], right[0]))
            se = len(va) - 1

        print('co=', co)
    return co

if __name__ == "__main__":
    T = int(input())
    for i in range(1, T+1):
        N = int(input())
        va = input()
        va = list(map(str, va))
        v = calcAns('left', va)
        k = calcAns('right', va)
        print("Case #{}: {}".format(i, (v, k)))