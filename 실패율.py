def solution(N, stages):
    fail = []
    users = [0]*(N+2)
    for stage in stages:
        users[stage] += 1
    for i in range(1, N+1):
        if users[i] != 0:
            fail.append([i , users[i] / (sum(users[i:]))])
        else:
            fail.append([i, 0])
    fail = list(map(lambda x: x[0], sorted(fail, key=lambda x: -x[1])))
    return fail