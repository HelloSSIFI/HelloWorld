def solution(s):
    answer = set()

    if len(s) == 1:
        return 1

    for i in range(1, len(s)+1):
        txt = s[:i]        # 검사 문자열
        cnt = 1            # 검사 문자열과 같은 문자배열의 개수
        pre = ''           # 검사하기 전 문자들을 담는 str

        for j in range(i, len(s)+i, i):
            if txt == s[j:j+i]:
                cnt += 1
            else:
                if cnt != 1:
                    pre += str(cnt) + txt
                else:
                    pre += txt

                txt = s[j:j+i]
                cnt = 1

        answer.add(len(pre))
    return min(answer)