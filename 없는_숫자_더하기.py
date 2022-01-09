def solution(numbers):
    lst = list(range(10))
    for number in numbers:
        lst[number] = 0
    return sum(lst)