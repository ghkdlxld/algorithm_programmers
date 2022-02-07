def solution(n, lost, reserve):
    students = [1]*(n+1)
    for number in lost:
        students[number] -= 1
    for number in reserve:
        students[number] += 1
    for i in range(1, n+1):
        if students[i] == 0:
            if (students[i-1] == 2 and (i < n and students[i+1] == 2)) or i == n :
                students[i-1] -= 1
                students[i] += 1
            elif students[i+1] == 2:
                students[i+1] -= 1
                students[i] += 1
            else:
                students[i-1] -= 1
                students[i] += 1
    return n-students.count(0)