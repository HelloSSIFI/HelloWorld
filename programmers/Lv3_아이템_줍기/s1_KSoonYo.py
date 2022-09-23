from collections import deque

def remove(MAP, left_up, right_down):

    # 현재 사각형 범위 내부에서 1인 곳 찾아서 지우기
    for i in range(right_down[1] + 1, left_up[1]):
        for j in range(left_up[0] + 1, right_down[0]):
            if MAP[i][j]:
                MAP[i][j] = 0

def draw(MAP, left_up, right_down):

    for i in range(right_down[1], left_up[1] + 1):
        for j in range(left_up[0], right_down[0] + 1):
            if not MAP[i][j]:
                MAP[i][j] = 1
 

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    MAP = [[0] * 101 for _ in range(101)]            # 0은 아무런 사각형도 채워져 있지 않은 상태


    # 사각형 그리기
    # 좌표 * 2를 해서 크기를 2배로 늘려줘야 너비나 높이차가 1인 사각형이라도 차가 2가 되기 때문에 두 테두리(왼쪽 or 오른쪽 이나 위 or 아래 의 경우) 중 겉 테두리만 쉽게 추출이 가능해짐

    for rec in rectangle:
        rec = list(map(lambda x : 2 * x, rec))
        left_down_x, left_down_y = rec[0], rec[1]
        right_up_x, right_up_y = rec[2], rec[3]

        # 좌측 상단부터 우측 하단까지 1로 채우기
        left_up_x, left_up_y = left_down_x, right_up_y
        right_down_x, right_down_y = right_up_x, left_down_y

        draw(MAP, (left_up_x, left_up_y), (right_down_x, right_down_y))

    for rec in rectangle:
        rec = list(map(lambda x : 2 * x, rec))

        left_down_x, left_down_y = rec[0], rec[1]
        right_up_x, right_up_y = rec[2], rec[3]


        # 좌측 상단부터 우측 하단까지 1로 채우기
        left_up_x, left_up_y = left_down_x, right_up_y
        right_down_x, right_down_y = right_up_x, left_down_y

        # 사각형 별 테두리 추출(내부 1 지우기)
        remove(MAP, (left_up_x, left_up_y), (right_down_x, right_down_y))

    q = deque([(characterY * 2, characterX * 2, 0)])
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    checked = [[False] * 101 for _ in range(101)]
    while q:
        y, x, dist = q.popleft()

        if (y, x) == (itemY * 2, itemX * 2):
            print(dist // 2)
            return dist // 2

        for d in dirs:
            ny = y + d[0]
            nx = x + d[1]
            if 0 < ny <= 100 and 0 < nx <= 100 and not checked[ny][nx] and MAP[ny][nx]:
                checked[ny][nx] = True
                q.append((ny, nx, dist + 1))
                

    return answer

solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8)
# solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 1, 3, 7, 8)