def solution(absolutes, signs):
    for (i, ab) in enumerate(absolutes):
        if not signs[i]:
            absolutes[i] = -ab
    return sum(absolutes)