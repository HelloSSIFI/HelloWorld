def solution(k, dungeons):
    answer = 0


    def dfs(k, cnt):                                            # 던전으로 순열을 만듬
        nonlocal answer
        answer = max(answer, cnt)                               # 탐험한 던전 갱신

        for i in range(len(dungeons)):                          # 모든 던전 길이만큼 순회
            if not visited[i] and k >= dungeons[i][0]:          # 방문하지 않은 던전이면서 최소 피로도를 만족하면
                visited[i] = 1                                  # 방문하고 재귀 후 다시 방문제거
                dfs(k - dungeons[i][1], cnt + 1)
                visited[i] = 0


    visited = [0] * len(dungeons)
    dfs(k, 0)
    return answer


# print(solution(80, [[80,20],[50,40],[30,10]]))
