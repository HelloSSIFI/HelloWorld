def remake(s):
    temp = []
    res = []
    word = ''

    for i in s:
        if i.isdigit():    # i가 숫자면 word에 추가
            word += i
        elif i == ',':    # ,가 나오면 더이상 이어지는 숫자가 없기 때문에 temp에 숫자로 변환 후 추가
            temp.append(int(word))
            word = ''    # word 초기화
        elif i == '{':    # 열린 괄호가 나오면 숫자가 시작,
            if temp:
                res.append(temp)
            temp = []    # temp 초기화

    temp.append(int(word))    # 남은 부분 처리
    res.append(temp)

    return res


def solution(s):
    answer = []
    s = remake(s)    # 입력받은 문자열 숫자로 바꿔주기

    s.sort(key=len)    # 요소의 길이순으로 정렬하기

    for i in s:    # 2차원 배열 순회하면서 answer에 중복값이 없게 담아주기
        for j in i:
            if j not in answer:
                answer.append(j)

    return answer