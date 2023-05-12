def solution(n, words):
    answer = [0, 0]    # [번호, 차례]
    check = set()    # 중복 단어 체크
    bf = words[0][0]    # 앞 단어 마지막 글자

    for idx, word, in enumerate(words):
        if (word not in check) and (word[0] == bf):    # 중복단어가 아니며 끝말잇기가 제대뢰 이루어진 경우
            check.add(word)    # 중복단어 목록에 단어 추가
            bf = word[-1]    # 마지막 글자 갱신
        else:    # 위 조건 중 하나라도 이루어지지 않은 경우
            num = idx % n + 1    # 번호
            answer = [num, (idx+n-num+1)//n]    # 정답 갱신
            break

    return answer