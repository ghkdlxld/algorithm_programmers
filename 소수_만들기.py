from itertools import combinations
def is_sosu(num):
    for i in range(2, num//2 + 1):
        if num%i == 0:
            return False
    return True

def solution(nums):
    ans = 0
    arr = list(combinations(nums, 3))
    for numbers in arr:
        if is_sosu(sum(numbers)):
            ans += 1
    return ans