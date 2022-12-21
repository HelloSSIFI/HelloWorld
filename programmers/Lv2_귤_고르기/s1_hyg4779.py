def solution(k, tangerine):
    answer = 0

    # 귤 크기별 개수 저장
    tangerine_cnt = {}
    for i in tangerine:
        tangerine_cnt[i] = tangerine_cnt[i] + 1 if tangerine_cnt.get(i, 0) else 1

    # (크기, 개수) 크기 내림차순으로 정렬
    info = sorted(list(tangerine_cnt.items()), key=lambda x: x[1], reverse=True)

    # 큰 것부터 제거하면서 개수 카운트
    while k:
        size, cnt = info.pop(0)
        answer += 1

        if cnt >= k:
            break

        else:
            k -= cnt
    print(answer)
    return answer

solution(6, [1, 3, 2, 5, 4, 5, 2, 3])
solution(4, [1, 3, 2, 5, 4, 5, 2, 3])
solution(2, [1, 1, 1, 1, 2, 2, 2, 3])
