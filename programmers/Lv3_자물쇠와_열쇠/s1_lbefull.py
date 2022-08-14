def rot():                                                  # key를 90도 회전하는 함수
    arr = [[0] * M for _ in range(M)]
    for r in range(M):
        for c in range(M):
            arr[r][c] = new_key[M - 1 - c][r]
    return arr


def solution(key, lock):
    global M, new_key
    N = len(lock)
    M = len(key) + 2 * (N - 1)
    new_key = [[0] * M for _ in range(M)]                   # 키를 양옆으로 자물쇠길이 -1 씩 늘려서
    for r in range(N - 1, N - 1 + len(key)):                # 새로운 키 배열의 각각 N * N 영역에 자물쇠를 대보면서 진행
        for c in range(N - 1, N - 1 + len(key)):            # 새로운 키를 만들어주는 부분
            new_key[r][c] = key[r - N + 1][c - N + 1]

    for _ in range(4):                                      # 90도씩 4번 회전
        for i in range(N - 1, M):                           # 키의 각각 N * N 영역을 확인하면서
            for j in range(N - 1, M):                       # 둘다 돌기이거나 둘다 홈이면 다음반복
                flag = False                                # for문이 모두 실행되었다면 True를 리턴
                for r in range(i - N + 1, i + 1):
                    for c in range(j - N + 1, j + 1):
                        if lock[r - i + N - 1][c - j + N - 1] == 1 and new_key[r][c] == 1:
                            flag = True
                            break
                        if lock[r - i + N - 1][c - j + N - 1] == 0 and new_key[r][c] == 0:
                            flag = True
                            break
                    if flag:
                        break
                else:
                    return True
        new_key = rot()
    return False
