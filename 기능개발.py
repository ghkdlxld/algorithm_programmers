def solution(progresses, speeds):
    left = []
    for i in range(len(progresses)):
        tmp = (100-progresses[i])//speeds[i]
        if (100-progresses[i])%speeds[i] > 0:
            tmp += 1
        left.append(tmp)
    print(left)
    idx = 0
    ref = 0
    ans = []
    while True:
        if idx == len(left)-1:
            ans.append(len(left))
            break
        elif left[ref] < left[idx+1]:
            ans.append(len(left[:idx+1]))
            left = left[idx+1:]
            idx = 0
            ref = 0
        else:
            idx += 1
    return ans