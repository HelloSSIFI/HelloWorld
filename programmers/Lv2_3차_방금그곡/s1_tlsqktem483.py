import math


def solution(m, musicinfos):
    cnt = 0
    answer = "(None)"
    music_list = {}
    input_code = ''
    for i in range(len(m)):
        if m[i] != '#':
            if i < len(m) - 1 and m[i+1] == '#':
                input_code += m[i].lower()
            else:
                input_code += m[i]

    for music in musicinfos:
        music = music.split(',')
        start_h, start_m = int(music[0][:2]), int(music[0][3:])
        end_h, end_m = int(music[1][:2]), int(music[1][3:])
        start, end = 60*start_h + start_m, 60*end_h + end_m
        gap = end - start
        code = ''
        for i in range(len(music[3])):
            if music[3][i] != '#':
                if i < len(music[3]) - 1 and music[3][i + 1] == '#':
                    code += music[3][i].lower()
                else:
                    code += music[3][i]
        code = code * (math.ceil(gap/len(code)))
        music_list[code[:gap]] = music[2]

    for k, v in music_list.items():
        if input_code in k:
            if answer == "None":
                answer = v
                cnt = len(k)
            else:
                if len(k) > cnt:
                    answer = v
                    cnt = len(k)
    return answer


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CCB", ["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"]))