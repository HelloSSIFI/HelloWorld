from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            q = deque([i])      
            while q:
                node = q.popleft()
                
                for i in range(n):
                    if node == i:
                        continue
                    if computers[node][i] and not visited[i]:
                        visited[i] = 1
                        q.append(i)

    return answer