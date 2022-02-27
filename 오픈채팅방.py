def solution(record):
    messages = []
    user_id = {}
    for i in record:
        if len(i.split()) == 3:
            m, user, name = i.split()
            user_id[user] = name
            messages.append([user, m])
        else:
            m, user = i.split()
            messages.append([user, m])
    ans = []
    for message in messages:
        if message[1] == 'Enter':
            ans.append(f'{user_id[message[0]]}님이 들어왔습니다.')
        elif message[1] == 'Leave':
            ans.append(f'{user_id[message[0]]}님이 나갔습니다.')
    return ans