def binary(num, n):
    ref = 0 * n
    ans = ''
    while num > 0:
        ans = str(num % 2) + ans
        num = num // 2
    return ans


def solution(n, arr1, arr2):
    map = []
    for i in range(n):
        map(int, list(binary(arr1[i], n)))
        map(int, list(binary(arr2[i], n)))

    return 0