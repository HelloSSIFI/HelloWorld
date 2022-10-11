def solution(s):
    answer = []
    for i in range(len(s)):
        change = []
        cnt = 0
        for j in range(len(s[i])):                                      # s의 i번째 요소 문자열에서
            change.append(s[i][j])                                      # 110 을 모두 제거하고
            while change[-3:] == ['1', '1', '0']:                       # 제거한 개수를 저장
                for _ in range(3):                                      # 110을 제거한 뒤 생기는 110도 제거
                    change.pop()
                cnt += 1
        
        c = 0
        for j in range(len(change)):                                    # 제거한 뒤 문자열을 순회
            if change[j] == '0':                                        # 1이 연속적으로 3번 반복되거나
                c = 0                                                   # 맨 마지막에 1로 끝나거나 11로 끝난다면

            elif change[j] == '1':                                      # 해당 1의 시작점 인덱스를 저장하고
                c += 1                                                  # 그 위치에 제거했던 110을 모두 넣어줌

            if c == 3:
                break

        j -= c - 1
        change = change[:j] + ['1', '1', '0'] * cnt + change[j:]
        answer.append(''.join(change))
    return answer


# print(solution(["1110", "100111100", "0111111010"]))
