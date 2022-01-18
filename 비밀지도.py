def trans(n):
    if n == '1':
        return '#'
    else:
        return ' '

def solution(n, arr1, arr2):
    ans = []
    for i in range(n):
        tmp = bin(arr1[i]|arr2[i])[2:]
        line = '0'*(n-len(tmp)) + tmp
        x = ''.join(map(trans, list(line)))
        ans.append(x)
    return ans