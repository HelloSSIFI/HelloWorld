def solution(want, number, discount):
    answer = 0
    N = len(discount)
    M = len(want)
    cnt = dict()
    fin = set()

    for i in range(M):
        cnt[want[i]] = number[i]                                    # 사야할 물품과 개수를 딕셔너리에 저장

    for i in range(N):
        if discount[i] in cnt:                                      # 모든 날짜 확인
            cnt[discount[i]] -= 1                                   # i일 물품이 원하는 물품이면 개수 카운트
            if cnt[discount[i]] <= 0: fin.add(discount[i])          # 모두 구입했다면 셋에 넣어줌

        if i > 9 and discount[i - 10] in cnt:                       # i - 10일 물품이 원했던 물품이면 개수에서 빼주고
            cnt[discount[i - 10]] += 1                              # 구입 개수가 부족해지면 셋에서 빼줌
            if cnt[discount[i - 10]] > 0: fin.discard(discount[i - 10])

        if len(fin) == M: answer += 1

    return answer


# print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
