from itertools import product


def solution(clockHands):
    answer = 9876543210
    n = len(clockHands)

    dy = [-1, 1, 0, 0, 0]
    dx = [0, 0, -1, 1, 0]

    def rotate(a, b, t, arr):
        for k in range(5):
            y, x = a + dy[k], b + dx[k]
            if 0 <= y < n and 0 <= x < n:
                arr[y][x] = (arr[y][x] + t) % 4

    for case in product(range(4), repeat=n):    # 첫째줄 최대4번까지 회전 한다는 가정 하에 모든 경우의 수를 만든다.
        arr = [i[:] for i in clockHands]    # 깊은 복사는 deepcopy 보다 slicing 이 빠름

        for j in range(n):    # case 를 가지고 첫번째 줄만 회전 시킨다
            rotate(0, j, case[j], arr)

        result = sum(case)    # 첫번째 줄 조작 횟수의 합

        for i in range(1, n):    # 두번째 줄부터 체크
            for j in range(n):
                if arr[i-1][j]:    # 12시 가있지 않은 시계만 조작
                    temp = 4 - arr[i-1][j]    # 12시에 가도록 하기 위한 조작 횟수
                    rotate(i, j, temp, arr)    # 회전
                    result += temp    # 조작 횟수 누적

        if sum(arr[n-1]):    # 마지막 라인에 12시를 향하지 않는 시계가 존재
            continue    # pass

        answer = min(answer, result)    # 시계가 모두 12시를 가리킨다면 answer을 최솟값으로 갱신

    return answer