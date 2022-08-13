from collections import deque
import copy


def move(s, d, n1, n2):
    rc = [0, 0]
    for rc[1] in range(s, s + d * N, d):                                        # 한쪽방향으로 밀면서
        Q = deque()                                                             # 같은 숫자가 붙어있으면 합쳐주는 함수
        for rc[0] in range(s, s + d * N, d):
            if arr[rc[n1]][rc[n2]]:                                             # 한 줄 방향을 정해서
                if Q and Q[-1][0] == arr[rc[n1]][rc[n2]] and Q[-1][1]:          # Q에 넣어줌
                    Q[-1][0] *= 2                                               # 만약 이전에 들어온 숫자가 같고 한번도 합쳐지지 않았다면
                    Q[-1][1] = 0                                                # 합쳐주고 현재 숫자는 버림
                else:
                    Q.append([arr[rc[n1]][rc[n2]], 1])
        
        for rc[0] in range(s, s + d * N, d):                                    # 다시 위에서 반복한 줄들을 순회
            if Q:                                                               # Q가 있다면 Q에서 숫자를 넣어주고
                arr[rc[n1]][rc[n2]] = Q.popleft()[0]                            # Q가 비었다면 0을 넣어줌
            else:
                arr[rc[n1]][rc[n2]] = 0


def dfs(cnt):
    global arr, result                                                          # 5번까지 dfs 탐색
    if cnt == 5:                                                                # 5번 이동했다면
        for i in range(N):                                                      # 최대값 갱신
            result = max(result, max(arr[i]))
        return

    arr_copy = copy.deepcopy(arr)                                               # arr을 복사해두고
    for i in range(2):                                                          # 아니라면
        for s, d in [[0, 1], [N - 1, -1]]:                                      # move 함수에 각각 상하좌우로 밀도록 값을 넣어주고
            move(s, d, i, ((i + 1) % 2))                                        # cnt+1 한 뒤 다시 dfs 탐색
            dfs(cnt + 1)                                                        # arr을 다시 원상복구
            arr = copy.deepcopy(arr_copy)

N = int(input())
arr = [list(map(int ,input().split())) for _ in range(N)]
result = 0
dfs(0)
print(result)
