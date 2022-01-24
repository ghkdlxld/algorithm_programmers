def solution(dartResult):
    area = {"S":1, "D":2, "T":3}
    arr = []
    i = 0
    while i < len(dartResult):
        if dartResult[i].isdigit() and dartResult[i+1].isdigit():
            arr.append("10")
            i += 2
        else:
            arr.append(dartResult[i])
            i += 1
    stack = []
    for dart in arr:
        if dart.isdigit():
            stack.append(int(dart))
        elif dart in area:
            stack[-1] = stack[-1]**area[dart]
        elif dart == '*':
            if len(stack) > 1:
                stack[-2] = stack[-2]*2
            stack[-1] = stack[-1]*2
        else:
            stack[-1] = -stack[-1]
    return sum(stack)