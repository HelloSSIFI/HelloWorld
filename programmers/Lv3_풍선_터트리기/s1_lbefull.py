def solution(a):
    N = len(a)
    min_v = 2000000000
    min_i = 0
    for i in range(N):                              # 최소값 인덱스를 min_i로 저장
        if min_v > a[i]:
            min_v = a[i]
            min_i = i

    answer = set([0, N - 1, min_i])                 # 최소값과 양 끝의 값은 끝까지 살아남을 수 있음
    min_v = a[0]
    for i in range(1, min_i):                       # min_i의 왼쪽 범위 탐색
        if min_v > a[i]:                            # 현재 탐색중인 i보다 왼쪽 위치에
            answer.add(i)                           # i보다 작은 값이 없다면 i는 최후까지 남을 수 있음
            min_v = a[i]

    min_v = a[N - 1]
    for i in range(N - 2, min_i, -1):               # min_i의 오른쪽도 마찬가지로 탐색
        if min_v > a[i]:
            answer.add(i)
            min_v = a[i]

    return len(answer)


# print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))
