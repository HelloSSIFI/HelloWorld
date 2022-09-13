from collections import deque

def solution(brown, yellow):
    answer = []

    visited = [[False] * 5001 for _ in range(5001)]

    q = deque([(3, 3, 8, 1, 1, 1)])   # (카펫 가로, 카펫 세로, 갈색 수, 노란색 수, 노란색 가로, 노란색 세로)
    while q:
        r, c, b, y, y_r, y_c = q.popleft()
        
        if b == brown and y == yellow:
            answer = [r, c]
            break

        # 노란색을 가로로 늘리는 경우 -> 현재 노란색 세로만큼 노란색 개수 +, 노란색 가로 + 1, 카펫 가로 + 1, 갈색 수 + 2 
        # 노란색을 세로로 늘리는 경우 -> 현재 노란색 가로만큼 노란색 개수 +, 노란색 세로 + 1, 카펫 세로 + 1, 갈색 수 + 2
        case1 = (r + 1, c, b + 2, y + y_c, y_r + 1, y_c)
        case2 = (r, c + 1, b + 2, y + y_r, y_r, y_c + 1)
        for nr, nc, nb, ny, ny_r, ny_c in [case1, case2]:
            if ny <= yellow and nb <= brown and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr, nc, nb, ny, ny_r, ny_c))

    return answer