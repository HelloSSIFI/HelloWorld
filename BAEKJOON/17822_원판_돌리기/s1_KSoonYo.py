import sys
from collections import deque

input = sys.stdin.readline

def avg(N, M, circles):
    total = 0
    n = 0
    result = 0
    for i in range(1, N + 1):
        for j in range(M):
            if circles[i][j]:
                total += circles[i][j]
                n += 1
    if n:
        result = total / n
    
    return result

def circles_total(N, circles):
    result = 0
    for i in range(1, N + 1):
        result += sum(circles[i])
    return result 


N, M, T = map(int, input().split())
circles = [[0] * M]

for _ in range(N):
    circles.append(deque(list(map(int, input().split()))))

for _ in range(T):
    x, d, k = map(int, input().split())
    k %= M
    if not k :
        continue

    temp = x
    while x <= N:
        # 원판 회전
        if d:
            # 반시계방향
            # 왼쪽으로 슬라이딩
            # circles[x] = circles[x][1:] + [circles[x][0]]
            circles[x].rotate(-k)
        else:
            # 시계 방향
            # 오른으로 슬라이딩
            # circles[x] = [circles[x][-1]] + circles[x][:M-1]
            circles[x].rotate(k)

        x += temp    
    

    # 인접한 수가 같은지 확인  
    # 같은 원판 내 인접한 수
    removed = False
    removed_list = set()
    for i in range(1, N + 1):
        for j in range(M - 1):
            # 일단 오른쪽 시계 방향으로만 체크
            if circles[i][j] and circles[i][j + 1] and circles[i][j] == circles[i][j + 1]:
                removed_list.add((i, j))
                removed_list.add((i, j + 1))
        # 원판의 양쪽 끝 열 체크
        if circles[i][0] and circles[i][-1] and circles[i][0] == circles[i][-1]:
            removed_list.add((i, 0))
            removed_list.add((i, M - 1))

    # 다른 원판에 인접한 수 -> 같은 열에 있는 인접한 수
    for j in range(M):
        for i in range(1, N):
            if circles[i][j] and circles[i + 1][j] and circles[i][j] == circles[i + 1][j]:
                removed_list.add((i, j))
                removed_list.add((i + 1, j))

    if removed_list:
        removed = True
        for removed_r, removed_c in removed_list:
            circles[removed_r][removed_c] = 0

    if not removed:
        average = avg(N, M, circles)
        for i in range(1, N + 1):
            for j in range(M):
                if circles[i][j] and circles[i][j] > average:
                    circles[i][j] -= 1
                elif circles[i][j] and circles[i][j] < average:
                    circles[i][j] += 1

print(circles_total(N, circles))




#######
### bfs로 인접한 점을 0으로 만든 풀이 -> 테스트케이스는 통과하지만 오답처리(원인 모름)
###
# import sys
# from collections import deque

# input = sys.stdin.readline


# def remover(N, M, circles, start):
#     hr, hc = start

#     dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
#     q = deque([(hr, hc)])
#     target = circles[hr][hc]
#     flag = False
#     while q:
#         r, c = q.popleft()

#         if (r, c) != start and circles[r][c] == target:
#             circles[r][c] = 0
#             flag = True

#         for d in dirs:
#             nr = r + d[0]
#             nc = c + d[1]
#             if nc < 0:
#                 nc = M - 1
#             elif nc >= M:
#                 nc = 0

#             if 0 < nr <= N  and  circles[nr][nc] == target:
#                 q.append((nr, nc))
#     if flag:
#         circles[hr][hc] = 0
        
#     return flag

# def avg(N, M, circles, survived=[]):
#     total = 0
#     n = 0
#     for i in range(1, N + 1):
#         for j in range(M):
#             if circles[i][j]:
#                 total += circles[i][j]
#                 n += 1
#                 survived.append((i, j))
#     result = 0
#     if n:
#         result = total / n
    
#     return result, survived

# def circles_total(N, circles):
#     result = 0
#     for i in range(1, N + 1):
#         for j in range(M):
#             if circles[i][j]:
#                 result += circles[i][j]
#     return result 


# N, M, T = map(int, input().split())
# circles = [[0] * M]

# for _ in range(N):
#     circles.append(deque(list(map(int, input().split()))))

# for _ in range(T):
#     x, d, k = map(int, input().split())
#     k %= M
#     if not k :
#         continue

#     temp = x
#     while x <= N:
#         # 원판 회전
#         if d:
#             # 반시계방향
#             # 왼쪽으로 슬라이딩
#             # circles[x] = circles[x][1:] + [circles[x][0]]
#             circles[x].rotate(-k)
#         else:
#             # 시계 방향
#             # 오른으로 슬라이딩
#             # circles[x] = [circles[x][-1]] + circles[x][:M-1]
#             circles[x].rotate(k)

#         x += temp    
#     # print('after roatation: ', circles)
#     # 인접한 수가 같은지 확인  
#     removed = False
#     for i in range(1, N + 1):
#         for j in range(M):
#             if circles[i][j]:
#                 if remover(N, M, circles, (i, j)):
#                     removed = True    
#     # print('after removed: ', circles)
#     if not removed:
#         average, survived = avg(N, M, circles)
      
#         for pos in survived:
#             r, c = pos
#             if circles[r][c] > average:
#                 circles[r][c] -= 1
#             elif circles[r][c] < average:
#                 circles[r][c] += 1
#         # print('after averaging: ', circles)
# # print('final: ',  circles)

# print(circles_total(N, circles))
