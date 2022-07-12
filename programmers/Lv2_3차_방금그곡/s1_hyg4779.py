def solution(m, musicinfos):
    answer = None
    # 시작, 끝, 곡이름, 멜로디
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")

    for now in musicinfos:
        s, e, name, tmp = now.split(',')
        tmp = tmp.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")

        sh, sm = s.split(':')
        eh, em = e.split(':')

        s = int(sh)*60+int(sm)
        e = int(eh)*60+int(em)

        time = e-s


        tmp *= time//len(tmp)+1
        tmp = tmp[:time]


        if m in tmp:
            if answer == None or answer[1] < time or (answer[1] == time and answer[2] > s):
                answer = (name, time, s)


    if answer:
        return answer[0]

    return "(None)"


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
