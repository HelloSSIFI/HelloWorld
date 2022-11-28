import sys
input = sys.stdin.readline


# 부메랑이 나올 수 있는 4가지 경우에 대해 체크하여 재귀 호출
# 부메랑으로 사용된 부분에 대해서 방문 체크
def search(N, M, i, j, woods, visited, temp = 0):
    global maxV

    if j == M:
        j = 0
        i += 1

    if i == N:
        maxV = max(maxV, temp)
        return

    if not visited[i][j]:
        if i + 1 < N and j + 1 < M:
            if not visited[i + 1][j] and not visited[i][j + 1]:
                visited[i][j], visited[i + 1][j], visited[i][j + 1] = [True, True, True]
    
                search(N, M, i, j + 1, woods, visited, temp + (woods[i][j] * 2) + woods[i + 1][j] + woods[i][j + 1])
                visited[i][j], visited[i + 1][j], visited[i][j + 1] = [False, False, False]

        if i + 1 < N and 0 <= j - 1:
            if not visited[i + 1][j] and not visited[i][j - 1]:
                visited[i][j], visited[i + 1][j], visited[i][j - 1] = [True, True, True]

                search(N, M, i, j + 1, woods, visited, temp + (woods[i][j] * 2) + woods[i + 1][j] + woods[i][j - 1])
                visited[i][j], visited[i + 1][j], visited[i][j - 1] = [False, False, False]

        if 0 <= i - 1 and j + 1 < M:
            if not visited[i - 1][j] and not visited[i][j + 1]:
                visited[i][j], visited[i - 1][j], visited[i][j + 1] = [True, True, True]

                search(N, M, i, j + 1, woods, visited, temp + (woods[i][j] * 2) + woods[i - 1][j] + woods[i][j + 1])
                visited[i][j], visited[i - 1][j], visited[i][j + 1] = [False, False, False]

        if 0 <= i - 1 and 0 <= j - 1:
            if not visited[i - 1][j] and not visited[i][j - 1]:
                visited[i][j], visited[i - 1][j], visited[i][j - 1] = [True, True, True]

                search(N, M, i, j + 1, woods, visited, temp + (woods[i][j] * 2) + woods[i - 1][j] + woods[i][j - 1])
                visited[i][j], visited[i - 1][j], visited[i][j - 1] = [False, False, False]

    search(N, M, i, j + 1, woods, visited, temp)
    return



N, M = map(int, input().split())
woods = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

maxV = 0
search(N, M, 0, 0, woods, visited)
print(maxV)        


# 시간 초과(이중 포문을 사용하지 않아야 함)

# def search(N, M, i, j, woods, visited, temp = 0):
#     global maxV

#     for i in range(N):
#         for j in range(M):
#             # 현재 지점을 중심으로 해서 가능한 경우의 수는 모두 4가지
#             if i + 1 < N and j + 1 < M:
#                 if not visited[i][j] and not visited[i + 1][j] and not visited[i][j + 1]:
#                     visited[i][j], visited[i + 1][j], visited[i][j + 1] = [True, True, True]
#                     search(N, M, woods, visited, temp + (woods[i][j] * 2) + woods[i + 1][j] + woods[i][j + 1])
#                     visited[i][j], visited[i + 1][j], visited[i][j + 1] = [False, False, False]

#             if i + 1 < N and 0 <= j - 1:
#                 if not visited[i][j] and not visited[i + 1][j] and not visited[i][j - 1]:
#                     visited[i][j], visited[i + 1][j], visited[i][j - 1] = [True, True, True]
#                     search(N, M, woods, visited, temp + (woods[i][j] * 2) + woods[i + 1][j] + woods[i][j - 1])
#                     visited[i][j], visited[i + 1][j], visited[i][j - 1] = [False, False, False]

#             if 0 <= i - 1 and j + 1 < M:
#                 if not visited[i][j] and not visited[i - 1][j] and not visited[i][j + 1]:
#                     visited[i][j], visited[i - 1][j], visited[i][j + 1] = [True, True, True]
#                     search(N, M, woods, visited, temp + (woods[i][j] * 2) + woods[i - 1][j] + woods[i][j + 1])
#                     visited[i][j], visited[i - 1][j], visited[i][j + 1] = [False, False, False]

#             if 0 <= i - 1 and 0 <= j - 1:
#                 if not visited[i][j] and not visited[i - 1][j] and not visited[i][j - 1]:
#                     visited[i][j], visited[i - 1][j], visited[i][j - 1] = [True, True, True]
#                     search(N, M, woods, visited, temp + (woods[i][j] * 2) + woods[i - 1][j] + woods[i][j - 1])
#                     visited[i][j], visited[i - 1][j], visited[i][j - 1] = [False, False, False]


#     if temp > maxV:
#         maxV = temp

#     return 

