import copy


def rotate(key):
    n = len(key)    # 열쇠 배열의 길이
    temp = [[0] * n for _ in range(n)]

    for a in range(n):
        for b in range(n):
            temp[b][n-a-1] = key[a][b]

    return temp


def check(test, n):
    for i in range(n, n*2):
        for j in range(n, n*2):
            if test[i][j] != 1:
                return False
    return True


def solution(key, lock):
    answer = True
    m = len(key)
    n = len(lock)
    # 현 자물쇠를 센터에 두고 열쇠 테스트(열쇠가 영역 벗어나도 됨) 하기 위해 가로, 세로 길이 각 3배가 되는 자물쇠를 만든다.
    test = [[0] * (n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            test[n+i][n+j] = lock[i][j]    # 기존 자물쇠 센터에 배치

    for i in range(1, n*2):
        for j in range(1, n*2):
            # 열쇠를 90도씩 회전하면서 열쇠가 자물쇠에 맞는지 확인
            cnt = 0
            while cnt < 4:
                test_copy = copy.deepcopy(test)
                key = rotate(key)    # 열쇠 90도 회전
                for y in range(m):
                    for x in range(m):
                        test_copy[i+y][j+x] += key[y][x]    # 자물쇠, 열쇠 합치기

                answer = check(test_copy, n)    # 자물쇠 부분이 전부 1이 되는지 확인

                if answer:
                    return answer

                cnt += 1

    return answer