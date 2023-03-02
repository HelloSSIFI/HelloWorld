def solution(begin, target, words):
    answer = 51
    length = len(begin)

    def check(now, cnt, visited):
        nonlocal answer, length

        if now == target or cnt > answer:    # 단어가 target이 되었으면 answer을 변환 단계 카운트로 갱신
            if cnt < answer:                 # cnt가 answer보다 큰 경우 더 이상 탐색할 필요가 없기 때문에 return
                answer = cnt
            return

        for word in words:
            if word in visited:              # 이미 변환한 단어는 pass
                continue

            tmp = length
            for i in range(length):
                if now[i] != word[i]:
                    tmp -= 1

            if tmp == length - 1:
                visited.append(word)         # 변환목록에 단어 추가
                check(word, cnt+1, visited)  # 재귀
                visited.pop()                # 추가 했던 단어 빼기

    for word in words:
        tmp = length
        for i in range(length):              # 불일치하는 단어면 tmp에서 -1
            if begin[i] != word[i]:
                tmp -= 1

        if tmp == length - 1:                # 하나의 알파벳만 다르다면 check를 통해 다음 변환 진행
            check(word, 1, [begin, word])

    if answer == 51:                         # 변환할 수 없는 경우 0을 return
        return 0

    return answer