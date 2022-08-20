import copy
def rotate(deg, key, m):
    if not deg:
        return key
    result = copy.deepcopy(key)
    for i in range(m):
        for j in range(m):
            result[i][j] = key[m - j - 1][i]
    return result

def solution(key, lock):
    answer = False
    m = len(key)                                                                        # key의 길이
    n = len(lock)                                                                       # lock의 길이
    lock_plus = [[0] * (4 * n) for _ in range(4 * n)]                                   # 보드 확장, 탐색할 때 key의 범위가 보드를 넘어가지만 않으면 ok
    for i in range(n):                                                                  # 자물쇠 배치
        for j in range(n):
            lock_plus[i + n][j + n] = lock[i][j]
    degree = 0
    for _ in range(4):
        key = rotate(degree, key, m)                                          # key 회전
        for sr in range(2 * n):                                               # lock_plus에서 key의 행 시작점 범위, lock_plus의 0번째 행부터 자물쇠 마지막 행 n + n 까지
            for sc in range(2 * n):                                           # lock_plus에서 key의 열 시작점 범위, lock_plus의 0번째 열부터 자물쇠 마지막 열 n + n 까지   
                temp = set()
                collision = False        
                for k in range(m):                                            # key의 2차원 범위
                    for h in range(m):
                        if (n <= sr + k < 2 * n) and (n <= sc + h < 2 * n):                # 자물쇠 영역 내라면
                            if lock_plus[sr + k][sc + h] and key[k][h]:                    # 자물쇠 영역 내에서 충돌이 일어났다면
                                collision = True                                           # 해당 영역은 더 볼 것도 없으므로 break
                                break
                            if not lock_plus[sr + k][sc + h] and key[k][h]:                # 자물쇠에 흠이 있고, 열쇠에 돌기가 있다면
                                temp.add((sr + k, sc + h))                                 # 집합에 추가
                    if collision:
                        break
                else:                                                                # 충돌이 없었다면
                    flag = False
                    for i in range(n, 2 * n):                                        # 자물쇠에 모두 채워지는지 체크
                        for j in range(n, 2 * n):
                            if (i, j) in temp:                                       # temp에 있는 조합은 열쇠가 들어간 것이므로 continue
                                continue
                            if lock_plus[i][j] == 0:                                 # 자물쇠에 홈이 남아 있다면 열쇠가 끼워지지 않은 것이므로 break
                                flag = True
                                break
                        if flag:
                            break
                    else:                                                            # for 문을 break없이 모두 돌았다면 열쇠가 모두 끼워진 것이므로 True return
                        return True
        degree += 90

    return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))