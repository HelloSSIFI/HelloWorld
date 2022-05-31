def solution(record):
    user = {}                               # 유저 아이디를 key, 닉네임을 value로 저장
    answer = []

    for log in record:                      # record 순회
        logs = log.split()                  # record를 공백 기준으로 잘라서

        if len(logs) == 3:                  # 길이가 3이면
            user[logs[1]] = logs[2]         # 유저 아이디와 닉네임을 최신화
    
    for log in record:                      # 다시 record 순회
        logs = log.split()                  # 다시 공백기준으로 잘라서 행동에 맞게 말을 만들어서 넣어줌

        if logs[0] == 'Enter':
            answer.append(f'{user[logs[1]]}님이 들어왔습니다.')
        elif logs[0] == 'Leave':
            answer.append(f'{user[logs[1]]}님이 나갔습니다.')
    
    return answer


# a = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
# print(solution(a))
