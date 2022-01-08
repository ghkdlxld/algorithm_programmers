def solution(numbers, hand):
    answer = ''
    keypad = [[3, 1],]
    for i in range(3):
        for j in range(3):
            keypad.append([i, j])
    left = (3, 0)
    right = (3, 2)
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left = keypad[number]
        elif number in [3, 6, 9]:
            answer += 'R'
            right = keypad[number]
        else:
            L = abs(left[0] - keypad[number][0]) + abs(left[1] - keypad[number][1])
            R = abs(right[0] - keypad[number][0]) + abs(right[1] - keypad[number][1])
            if L < R:
                answer += 'L'
                left = keypad[number]
            elif L == R:
                if hand == "left":
                    answer += 'L'
                    left = keypad[number]
                else:
                    answer += 'R'
                    right = keypad[number]
            else:
                answer += 'R'
                right = keypad[number]
    return answer
