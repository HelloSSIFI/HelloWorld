def remove_hash(s):                     # #이 들어간 음을 한글자 다른 이름으로 치환
    new_s = ''
    for i in range(len(s) - 1):
        if s[i] == '#':                 # 현재 단어가 #이면 다음반복
            continue

        if s[i + 1] == '#':             # 다음 단어가 #이면
            if s[i] == 'A':             # 각각의 음계를 V~Z 로 치환
                new_s += 'Z'
            elif s[i] == 'C':
                new_s += 'Y'
            elif s[i] == 'D':
                new_s += 'X'
            elif s[i] == 'F':
                new_s += 'W'
            elif s[i] == 'G':
                new_s += 'V'
        else:
            new_s += s[i]
    
    if s[-1] != '#':                    # 마지막 단어가 #이 아니면 추가
        new_s += s[-1]
    
    return new_s


def solution(m, musicinfos):
    answer = '(None)'                                           # 정답 초기화
    music_dict = dict()                                         # 곡이름을 key, 시간과 악보 정보를 value로 저장

    new_m = remove_hash(m)
    for musicinfo in musicinfos:
        s, e, name, mel = musicinfo.split(',')

        times = []
        for time in [s, e]:
            hh, mm = time.split(':')                            # 시간 문자열을 정수 분으로 바꿔줌
            times.append(int(hh) * 60 + int(mm))

        mel = remove_hash(mel)
        new_mel = list(mel)
        i = 0
        while len(new_mel) < times[1] - times[0]:               # 곡 재생 시간보다 작을경우 재생 시간만큼 늘려줌
            new_mel.append(mel[i])
            i += 1
            if i == len(mel):
                i = 0

        if times[1] - times[0] < len(new_mel):                  # 곡 재생 시간보다 클 경우 재생 시간만큼 잘라줌
            new_mel = new_mel[:times[1] - times[0]]

        new_mel = ''.join(new_mel)
        
        music_dict[name] = (times[1] - times[0], new_mel)       # 딕셔너리에 알맞게 저장
    
    max_min = 0
    for k, v in music_dict.items():
        if new_m in v[1]:                                       # 현재 악보에 기억하는 음이 존재하고
            if max_min < v[0]:                                  # 이전에 저장한 악보보다 클 경우
                answer = k                                      # 현재 곡을 저장
                max_min = v[0]
    
    return answer

# print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
