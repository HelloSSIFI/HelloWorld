def solution(a):
    answer = set()    # 중복 값 배제를 위한 set
    n = len(a)
    left, right = 1000000001, 1000000001    # 각 방향 최솟값 갱신을 위한 초기값

    # 기준이 되는 idx의 -1, +1 모두 작다면 풍선 터트리기 불가능
    for i in range(n):
        if a[i] < left:    # 좌측 기준으로 최솟값 찾으면서 갱신
            left = a[i]
            answer.add(i)

        if a[n-1-i] < right:    # 우측 기준으로 최솟값 찾으면서 갱신
            right = a[n-1-i]
            answer.add(n-1-i)

    return len(answer)