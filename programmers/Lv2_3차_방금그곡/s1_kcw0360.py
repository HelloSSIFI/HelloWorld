def check(melody, info):
    res = []

    # 시작, 끝 시간의 차를 분으로 환산하여 재생시간 구하기
    hours = (int(info[1][0:2]) - int(info[0][0:2])) * 60
    minutes = int(info[1][3:5]) - int(info[0][3:5])
    time_diff = hours + minutes

    # 멜로디와 같이 곡의 음 정보를 리스트로 만들어 주기
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

    # 곡 재생시간을 통해 몇번 반복했으며 어느 구간까지 재생되었는지 확인 후 만들어 주기
    a, b = divmod(time_diff, len(pitch))
    pitch = pitch * a + pitch[:b]

    length = len(pitch) - len(melody)    # 기억하고 있는 부분과 재생된 곡의 음정보 길이 차이

    if length >= 0:    # 재생된 것의 음의 길이가 더 긴 경우
        for i in range(len(pitch)):    # 기억한 멜로디와 같은 길이로 자른 후 비교
            if pitch[i:i+len(melody)] == melody:
                res.append(time_diff)    # 같다면 결과 값에 시간, 곡 이름 저장
                res.append(info[2])
                break    # 찾았기 때문에 반복문 빠져 나오기

    return res


def solution(m, musicinfos):
    result = []

    # 멜로디를 리스트로 만들기 (#과 문자를 하나의 요소로 저장하기 위함)
    melody = []    # 기억한 멜로디 저장
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

    # 곡 정보 순회하면서 멜로디와 비교
    for i in musicinfos:
        temp = check(melody, i.split(','))
        if temp:    # temp가  빈 리스트가 아닐 경우 결과 값에 저장
            result.append(temp)

    # 빈 리스트면 (None) 출력
    # 존재 한다면 result의 곡 정보를 순회하면서 temp에 재생시간, answer에 곡명을 담으며 체크
    # 가장 긴 재생시간이며, 동시간 재생일 경우 먼저 언급된 곡을 결과 값으로 출력
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
