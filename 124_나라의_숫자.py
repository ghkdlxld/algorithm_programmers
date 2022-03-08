# 1
def solution(n):
    thr = ''
    while n > 0:
        tmp = n % 3
        if tmp == 0:
            thr = '4' + thr
        else:
            thr = str(tmp) + thr
        n -= 1
        n //= 3
    return thr

# 2
def solution(n):
    num = ['1', '2', '4']
    thr = ''
    while n > 0:
        n -= 1
        thr = num[n%3] + thr
        n //= 3
    return thr