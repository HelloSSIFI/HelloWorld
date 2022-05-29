def solution(record):

    records = []
    for rec in record:
        records += [list(rec.split())]    # 입력받은 문자열들 분리 한 후 하나의 리스트로 만들어 저장

    user_dict = {}    # userId : nickname

    for i in records:
        if i[0] == 'Enter':     # 입장했을 때 등록
            user_dict[i[1]] = i[2]
        elif i[0] == 'Change':    # nickname 변경
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