def remake(s):
    temp = []
    res = []
    word = ''
    for i in s:
        if i.isdigit():
            word += i
        elif i == ',':
            temp.append(int(word))
            word = ''
        elif i == '{':
            if temp:
                res.append(temp)
            temp = []
    temp.append(int(word))
    res.append(temp)
    return res


def solution(s):
    answer = []
    s = remake(s)
    st = s.copy()
    cnt = 1
    temp = []

    while cnt <= len(s):
        for i in st:
            if cnt == len(i):
                temp.append(i)
                st.remove(i)
                break
        cnt += 1

    for i in temp:
        for j in i:
            if j not in answer:
                answer.append(j)

    return answer