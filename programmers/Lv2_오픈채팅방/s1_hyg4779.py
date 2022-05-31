def solution(record):
    answer = []
    '''
    1. 채팅방을 나가서 새로운 닉네임으로 재접속
    2. 채팅방안에서 변경
    '''
    chat = list()       # 채팅 데이터
    users = dict()      # user ID 별 닉네임을 갱신해 줄 dict

    for arg in record:
        args = arg.split()

        if args[0] == 'Enter':
            # args[1]: ID, args[2]: Nick
            chat.append([args[1], args[2], '님이 들어왔습니다.'])
            users[args[1]] = args[2]            # 모든 user의 목록을 담음

        elif args[0] == 'Leave':
            # args[1]: ID
            chat.append([args[1], users[args[1]], '님이 나갔습니다.'])

        elif args[0] == 'Change':
            users[args[1]] = args[2]


    for line in chat:
        line[1] = users[line[0]]

        answer.append(f'{line[1]}{line[2]}')

    return answer