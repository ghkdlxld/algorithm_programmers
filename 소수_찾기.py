from itertools import permutations


def solution(numbers):
    def is_sosu(num):
        for i in range(2, int(num ** (0.5) + 1)):
            if num % i == 0:
                return False
        return True

    arr = []
    for i in range(1, len(numbers) + 1):
        tmp = list(permutations(numbers, i))
        for t in tmp:
            arr.append(int(''.join(t)))

    arr = list(set(arr))
    ans = 0
    for num in arr:
        if num != 0 and num != 1 and is_sosu(num):
            ans += 1
    return ans