def solution(record):
    user = {}
    temp = []
    ans = []
    for i in record:
        i = i.split()
        if i[0] != "Leave":
            user[i[1]] = i[2]
            if i[0] == "Enter":
                temp.append([i[1], "님이 들어왔습니다."])
            else:
                pass
        else:
            temp.append([i[1], "님이 나갔습니다."])
    for j in temp:
        j[0] = user[j[0]]
        ans.append(j[0]+j[1])
    return ans