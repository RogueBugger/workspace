def find_odd(n):
    '''N = str(n)
    flag = 0
    for n in N:
        if int(n) % 2 != 0:
            flag = 1 
            break

    return flag'''
    flag = 0
    temp = n
    print(temp)
    while(temp != 0):
        r = temp % 10
        if r % 2 != 0:
            flag = 1
            break
        temp = temp / 10
    print(flag)
    return flag

        
def calc_press(value, n):
    co = 0
    while True:
        co += 1
        n = n + value
        if find_odd(n) is 0:
            return co
T = int(input())    
for i in range(T):
    N = int(input())
    OPTION_1 = +1
    OPTION_2 = -1
    if find_odd(N) is 0:
        print("Case #{}: {}".format(i+1,0))
    else:
        OPTION_PLUS = calc_press(OPTION_1, N)
        OPTION_MINUS = calc_press(OPTION_2, N)
        print("Case #{}: {}".format(i+1,min(OPTION_PLUS, OPTION_MINUS)))
