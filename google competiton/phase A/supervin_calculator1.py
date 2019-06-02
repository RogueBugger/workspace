def calAns(N):
    def find_odd(n):
        flag = 0
        temp = n
        while(temp != 0):
            r = temp % 10
            if r % 2 != 0:
                flag = 1
                break
            temp = int(temp / 10)
        return flag

    def calc_press(value, n):
        co = 0
        while True:
            co += 1
            n = n + value
            if find_odd(n) is 0:
                return co
    OPTION_1 = +1
    OPTION_2 = -1

    if find_odd(N) is 0:
        ans = f"Case #{i+1}: 0"

    else:
        OPTION_PLUS = calc_press(OPTION_1, N)
        OPTION_MINUS = calc_press(OPTION_2, N)
        ans = f"Case #{i+1}: {min(OPTION_PLUS, OPTION_MINUS)}"

    return ans
    
if __name__ == "__main__":
    T = int(input())    
    for i in range(T):
        N = int(input())
        print(calAns(N))
''' N = str(n)
        flag = 0
        for n in N:
            if int(n) % 2 != 0:
                flag = 1 
                break
        return flag'''   