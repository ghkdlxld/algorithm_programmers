def solution(a, b):
    week = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    month = {1: 2, 2: 0, 3: 2, 4: 1,5: 2,6: 1,7: 2,8: 2,9: 1,10: 2,11: 1,12: 2}
    ans = 5-1
    for key,value in month.items():
        if key < a:
            ans += (value + 1)
    ans = week[(ans+b)%7]
    return ans