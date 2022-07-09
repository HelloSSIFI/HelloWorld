def check(melody, info):
    res = []

    hours = (int(info[1][0:2]) - int(info[0][0:2])) * 60
    minutes = int(info[1][3:5]) - int(info[0][3:5])
    time_diff = hours + minutes

    pitch = []
    tmp = ''
    for i in range(len(info[3])-1, -1, -1):
        if info[3][i] == '#':
            tmp += '#'
            continue

        if tmp:
            pitch = [info[3][i]+tmp] + pitch
            tmp = ''
        else:
            pitch = [info[3][i]+tmp] + pitch

    a, b = divmod(time_diff, len(pitch))
    pitch = pitch * a + pitch[:b]

    length = len(pitch) - len(melody)

    if length > 0:
        for i in range(len(pitch)):
            if pitch[i:i+len(melody)] == melody:
                res.append(time_diff)
                res.append(info[2])
                break
    elif length == 0:
        if pitch == melody:
            res.append(time_diff)
            res.append(info[2])
    if time_diff == 0:
        return []
    return res


def solution(m, musicinfos):
    result = []

    melody = []
    tmp = ''
    for i in range(len(m) - 1, -1, -1):
        if m[i] == '#':
            tmp += '#'
            continue

        if tmp:
            melody = [m[i] + tmp] + melody
            tmp = ''
        else:
            melody = [m[i] + tmp] + melody

    for i in musicinfos:
        temp = check(melody, i.split(','))
        if temp:
            result.append(temp)

    if result:
        temp = 0
        answer = ''
        for i in result:
            if temp < i[0]:
                temp = i[0]
                answer = i[1]
        return answer
    else:
        return '(None)'
