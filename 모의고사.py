def solution(answers):
    N = len(answers)
    pick = [ False ,'12345', '21232425', '3311224455']
    supoja = [False]*4
    for n in range(1, 4):
        supoja[n] = pick[n]*(N//len(pick[n])) + pick[n][:N%len(pick[n])]
    for n in range(1, 4):
        tmp = 0
        for i in range(N):
            if supoja[n][i] == str(answers[i]):
                tmp += 1
        pick[n] = tmp
    ans = []
    for i in range(1,4):
        if pick[i] == max(pick[1:]):
            ans.append(i)
    return ans