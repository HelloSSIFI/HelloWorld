def solution(k, tangerine):
    answer = 0
    cnt = dict()
    for i in range(len(tangerine)):                                 # 귤의 크기를 key로 하여 개수를 value에 저장
        cnt[tangerine[i]] = cnt.get(tangerine[i], 0) + 1
    cnt = sorted(cnt.values(), reverse=True)                        # 귤의 개수를 내림차순으로 정렬
    for c in cnt:                                                   # 귤의 개수를 순회
        k -= c                                                      # 현재 크기의 개수를 추가(k에서 빼줌)
        answer += 1                                                 # 크기의 종류가 1 증가
        if k <= 0:                                                  # k개를 넘어서면 반복 종료
            break
    return answer


# print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))
