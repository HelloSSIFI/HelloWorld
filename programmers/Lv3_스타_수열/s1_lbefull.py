def solution(a):
    answer = 0
    N = len(a)
    cnt = dict()
    for i in a:                                                         # 수열의 각 원소의 개수를 찾아줌
        cnt[i] = cnt.get(i, 0) + 1
    cnt = sorted(cnt.items(), key=lambda x: -x[1])                      # 원소의 개수가 많은 순서대로 정렬

    for n, c in cnt:
        max_l = min(c, N - c) * 2                                       # 스타 수열의 최대 길이는 현재 원소 개수 또는 나머지 원소 개수 중 적은것을 2배한 값과 같음
        if max_l < answer: break                                        # 최대 길이가 이미 구한 answer 보다 작아진다면 반복 종료

        l = 0
        visited = [0] * N
        for i in range(N):
            if a[i] != n: continue                                      # 현재 확인할 원소 n의 위치를 찾아줌

            if i > 0 and a[i - 1] != a[i] and not visited[i - 1]:       # n 이전의 원소가 n이 아니고 사용하지 않은 원소이면
                visited[i - 1] = visited[i] = 1                         # 두 개를 스타수열 원소로 사용하고 스타수열 길이를 2 늘려줌
                l += 2
            elif i < N - 1 and a[i] != a[i + 1]:                        # 이전 원소가 조건이 안맞다면 다음 원소를 확인
                visited[i] = visited[i + 1] = 1
                l += 2

        if answer < l: answer = l                                       # 현재 구한 스타수열 길이가 저장된 answer보다 크면 갱신하고
        if l == max_l: break                                            # 그 길이가 최대값일 경우 반복종료

    return answer


# print(solution([0, 3, 3, 0, 7, 2, 0, 2, 2, 0]))
