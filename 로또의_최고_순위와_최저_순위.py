# 1 내 풀이
def solution(lottos, win_nums):
    cnt = 0
    guess = lottos.count(0)
    for lotto_num in lottos:
        if lotto_num in win_nums:
            cnt += 1
    a, b = 0, 0
    if cnt+guess > 1:
        a = 7-(cnt+guess)
        if cnt > 1:
            b = 7-cnt
        else:
            b = 6
    else:
        a, b = 6, 6
    answer = [a, b]
    return answer

# 최적화 풀이
def solution(lottos, win_nums):
    cnt = 0
    guess = lottos.count(0)
    rank = [6, 6, 5, 4, 3, 2, 1]
    for lotto_num in lottos:
        if lotto_num in win_nums:
            cnt += 1

    answer = [rank[cnt + guess], rank[cnt]]
    return answer