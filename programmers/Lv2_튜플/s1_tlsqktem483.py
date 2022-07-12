from collections import defaultdict


def solution(s):
    answer = []
    n_list = []
    open = False
    temp = []
    temp_n = ''
    for i in range(1, len(s)-1):
        if s[i] == "{":
            temp = []
            temp_n = ''
            open = True
        elif s[i] == "}":
            temp.append(int(temp_n))
            n_list.append(temp)
            open = False
        elif open and s[i] == ",":
            temp.append(int(temp_n))
            temp_n = ''
        elif open and s[i].isnumeric():
            temp_n += s[i]

    n_dict = defaultdict(int)
    for numbers in n_list:
        for n in numbers:
            n_dict[n] += 1
    for t in sorted(n_dict.items(), key=lambda x: x[1], reverse=True):
        answer.append(t[0])

    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))