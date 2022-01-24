def solution(dartResult):
    arr = []
    i = 0
    while i < len(dartResult):
        if dartResult[i].isdigit() and dartResult[i+1].isdigit():
            arr.append(10)
            i += 2
        else:
            arr.append(dartResult[i])
            i += 1
    return arr