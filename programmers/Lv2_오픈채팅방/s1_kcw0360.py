def solution(record):

    records = []
    for rec in record:
        records += [list(rec.split())]
    user_dict = {}
    for i in records:
        if i[0] == 'Enter':
            user_dict[i[1]] = i[2]
        elif i[0] == 'Change':
            user_dict[i[1]] = i[2]


    answer = []
    for i in records:
        if i[0] == 'Enter':
            ans = '{}님이 들어왔습니다.'.format(user_dict[i[1]])
            answer.append(ans)
        elif i[0] == 'Leave':
            ans = '{}님이 나갔습니다.'.format(user_dict[i[1]])
            answer.append(ans)

    return answer