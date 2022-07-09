def solution(m, musicinfos):
    answer = '(None)'
    candidate = []                                                  # (음악 제목, 재생 시간, 들어온 순서) -> 재생 시간 별로 역순 정렬
    h = 0

    changed_m = ''
    j = -1
    for idx in range(len(m)):                                       # C# -> c 등 반음 치환
        if m[idx] == '#':
            changed_m = changed_m[:j] + m[idx - 1].lower()
            continue
        changed_m += m[idx]
        j += 1

    for music in musicinfos:
        info = music.split(',')
        s_h, s_m = info[0].split(':')
        e_h, e_m = info[1].split(':')
        music_title = info[2]                                       # 음악 제목
        music_notes = info[3]                                       # 음악 악보
        s = int(s_h) * 60 + int(s_m)
        e = int(e_h) * 60 + int(e_m)
        played_time = e - s

        changed_music_notes = ''
        k = -1
        for idx in range(len(music_notes)):                         # 반음 치환
            if music_notes[idx] == '#':
                changed_music_notes = changed_music_notes[:k] + music_notes[idx-1].lower()
                continue
            changed_music_notes += music_notes[idx]
            k += 1


        played_notes = ''                                           # 실제 연주된 음
        time = 0
        i = 0
        while time <= played_time:
            i = i % len(changed_music_notes)
            played_notes += changed_music_notes[i]
            print('played_notes: ', played_notes)
            time += 1
            i += 1

        if changed_m in played_notes:                               # 실제 연주된 음에 멜로디가 들어있다면
            candidate.append((music_title, played_time, h))
            h += 1 

    if candidate:
        candidate.sort(key=lambda x : (-x[1], x[2]))                #재생 시간이 가장 긴 순으로 내림차순 정렬 후 진입이 빠른 순으로 오름차순 정렬
        answer = candidate[0][0]
    return answer

