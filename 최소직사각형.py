def solution(sizes):
    sizes = list(map(sorted, sizes))
    ans = 1
    for i in range(2):
        ans *= max(sizes, key=lambda x:x[i])[i]
    return ans