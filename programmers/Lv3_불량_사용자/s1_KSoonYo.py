def check(origin, banned_id):
    if len(origin) != len(banned_id):
        return False

    temp = ''
    for char_idx in range(len(banned_id)):
        if banned_id[char_idx] == '*':
            temp += '*'
            continue
        temp += origin[char_idx]
    
    if temp == banned_id:
        return True
    return False

def dfs(table, idx, temp_set, banned_list, result, cnt = 0):
    if len(temp_set) == len(banned_list) and temp_set not in result:
        copied_set = temp_set.copy()
        result.append(copied_set)
        cnt += 1
        return cnt

    if idx >= len(banned_list):
        return cnt

    for candidate in table[banned_list[idx]]:
        if candidate not in temp_set:
            temp_set.add(candidate)
            cnt += dfs(table, idx + 1, temp_set, banned_list, result)
            temp_set.remove(candidate)
    return cnt

def solution(user_id, banned_id):
    answer = 0
    candidates_table = {}
    result = []
    for banned_user in banned_id:
        if not candidates_table.get(banned_user):
            candidates_table[banned_user] = []

        for user in user_id:
            if len(user) != len(banned_user):
                continue
            
            if user in candidates_table[banned_user]:
                continue
            
            if check(user, banned_user):
                candidates_table[banned_user].append(user)
    answer = dfs(candidates_table, 0, set(), banned_id, result)
    return answer

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
solution(["a", "bb","c"], ["*b"])
