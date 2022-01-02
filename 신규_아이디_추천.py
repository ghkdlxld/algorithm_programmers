# 내 풀이
def solution(new_id):
    new_id = list(new_id.lower())
    can = ['-', '_', '.']
    i = 0
    while i < len(new_id):
        if (not new_id[i].isalpha()) and (not new_id[i].isdigit()) and (new_id[i] not in can):
            new_id.pop(i)
        else:
            i += 1
    new_id = ''.join(new_id)
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    new_id = new_id.strip('.')
    if len(new_id) == 0:
        new_id = 'a'
    elif len(new_id) >= 16:
        new_id = new_id[:15]
    new_id = new_id.strip('.')
    if len(new_id) <= 2:
        new_id = new_id + new_id[-1]*(3-len(new_id))
    answer = new_id
    return answer


# 정규식 공부해보자..!