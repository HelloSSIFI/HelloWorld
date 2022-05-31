def solution(s):
    answer = len(s)                                             # 결과값 초기화
    for ref in range(1, len(s) // 2 + 1):                       # 최대 압축은 문자열 길이의 반이므로 반까지만 반복
        cnt = 0                                                 # 현재 문자열이 몇번 나왔는지 저장
        cur_len = len(s)                                        # 현재 압축 시 문자열 길이
        i = 0                                                   # 탐색 인덱스
        temp = ''                                               # 현재 인덱스의 이전 압축 문자열

        while i <= len(s):                                      # 문자열 길이만큼 반복
            if i + ref <= len(s) and temp == s[i:i + ref]:      # 이전 압축 문자열과 현재 문자열이 같으면
                cnt += 1                                        # cnt 1 증가
                cur_len -= ref                                  # 현재 압축길이만큼 빼주고
                i += ref                                        # 인덱스를 현재 압축 길이만큼 더해준 뒤 다음반복
                continue

            if cnt > 1:                                         # cnt가 2 이상이면
                cur_len += len(str(cnt))                        # 문자열 길이에서 cnt 숫자 길이만큼 더해줌

            if i + ref <= len(s):                               # 현재 탐색이 총 문자열 길이내에 있으면
                temp = s[i:i + ref]                             # temp를 현재 문자열로 바꿔주고
                cnt = 1                                         # cnt를 1로 초기화
            i += ref                                            # 인덱스에 압축 길이만큼 더해서 다음반복

        answer = min(answer, cur_len)                           # 반복이 끝난 후 answer과 비교해서 작은쪽을 선택
    return answer


# a = "ababcdcdababcdcd"
# print(solution(a))
