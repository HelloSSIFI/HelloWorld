# 시간 초과 fail

def change_nickname(before, after, history, uuid):
    new_history = []
    new_answer = []
    common_position = '님이'
    before_history = before + common_position
    after_history = after + common_position
    for line in history:
        if line[0] == uuid:
            parts = line[1].split()
            name_part = parts[0]
            behavior_part = parts[1]

            if before_history == name_part:
                name_part = after_history
            
            new_line = (line[0], name_part + ' ' + behavior_part )  
        else:
            new_line = line
        new_history.append(new_line)
        new_answer.append(new_line[1])
    return new_history, new_answer

def solution(records):
    user_dict = {}
    history = []

    answer = []
    for record in records:
        system_msg = record.split()
        uuid = system_msg[1]
        if system_msg[0] == 'Enter':
            if system_msg[1] in user_dict.keys():
                before_nickname = user_dict[system_msg[1]]
                after_nickname = system_msg[2]
                history, answer = change_nickname(before_nickname, after_nickname, history, uuid)
                user_dict[system_msg[1]] = system_msg[2]

            else:
                user_dict[system_msg[1]] = system_msg[2]
            
            line = f'{user_dict[system_msg[1]]}님이 들어왔습니다.'
            history.append((uuid, line))
            answer.append(line)

        elif system_msg[0] == 'Leave':
            nickname = user_dict[system_msg[1]]
            line = f'{nickname}님이 나갔습니다.' if nickname != system_msg[1] else f'{system_msg[1]}님이 나갔습니다.'
            history.append((uuid, line))
            answer.append(line)

        else:
            before_nickname = user_dict[system_msg[1]]
            after_nickname = system_msg[2]
            history, answer = change_nickname(before_nickname, after_nickname, history, uuid)
            user_dict[system_msg[1]] = system_msg[2]
        

    return answer


print(solution(["Enter uid1234 Muzi", 
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan"]))
