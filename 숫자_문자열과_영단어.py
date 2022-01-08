def solution(s):
    lst = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = ''
    for i in range(len(s)):
        if s[i].isdigit():
            answer += s[i]
        else:
            for j in lst:
                if s[i:i+len(j)] == j:
                    answer += str(lst.index(j))
                    break
    return int(answer)
