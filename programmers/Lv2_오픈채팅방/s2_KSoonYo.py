
def print_history(user_dict, record):
    return f'{user_dict[record[0]]}님이 ' + record[1]

def solution(records):
    user_dict = {}
    history = []

    for record in records:
        system_msg = record.split() # Enter uuid1234 Muzi -> ['Enter', 'uuid1234', 'Muzi']
        command = system_msg[0]
        action = ''
        uuid = system_msg[1]
        if command == 'Enter':
            action = '들어왔습니다.'
            nickname = system_msg[2]
            user_dict[uuid] = nickname
            history.append((uuid, action))
            
        elif command == 'Leave':
            action = '나갔습니다.'   
            history.append((uuid, action))
        else:
            new_nickname = system_msg[2]
            user_dict[uuid] = new_nickname        


    answer = []
    for record in history:
        answer.append(print_history(user_dict, record))

    return answer


