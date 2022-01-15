def solution(a, b):
    answer = 0
    for n in range(len(a)):
        answer += a[n]*b[n]
    return answer


# 다른풀이
def solution(a, b):
    return sum(x*y for x, y in zip(a,b))


def solution(a, b):
    return sum(map(lambda i: a[i]*b[i], range(len(a))))