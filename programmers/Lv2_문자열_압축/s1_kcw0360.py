def solution(s):
    answer = len(s)

    for i in range(1, len(s) // 2 + 1):    # 압축할 문자열 단위
        compress = ''    # 압축한 문자열 결과물
        cnt = 1    # 압축한 갯수

        for j in range(0, len(s), i):    # i개 단위로 체크
            if s[j:j+i] == s[j+i:j+2*i]:    # i개와 다음 i개가 일치 하는지 확인
                cnt += 1    # 같다면 카운트 +1
            else:
                if cnt >= 2:    # 카운트수가 2이상이면 압축되는 문자열 앞에 개수 추가하기
                    compress += str(cnt)
                compress += s[j:j+i]    # 단위 문자열 추가
                cnt = 1    # 카운트 초기화

        answer = min(answer, len(compress))    # 비교 후 문자열 길이가 작은 것으로 치환

    return answer