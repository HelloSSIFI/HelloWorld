import sys
input = sys.stdin.readline

dirs_F = [[0, 1], [0, -1], [-1, 0], [1, 0]]       # 좌표평면 상 하 좌 우(전진)
dirs_B = [[0, -1], [0, 1], [1, 0], [-1, 0]]       # 좌표평면 상 하 좌 우(후진)

turn_L = {
    0 : 2,
    1 : 3,
    2 : 1,
    3 : 0
}                                               # 반시계 방향 회전 테이블

turn_R = {
    0 : 3,
    1 : 2,
    2 : 0,
    3 : 1
}                                               # 시계 방향 회전 테이블

T = int(input())
answers = []
for _ in range(T):
    commands = input().strip()
    routes = [(0, 0)]
    here = (0, 0)
    d = 0
    for command in commands:
        x, y = here
        if command == 'F':
            x += dirs_F[d][0]
            y += dirs_F[d][1]
        elif command == 'B':
            x += dirs_B[d][0]
            y += dirs_B[d][1]
        elif command == 'L':
            d = turn_L[d]

        elif command == 'R':
            d = turn_R[d]
        
        if (x, y) != here and (x, y) not in routes:
            routes.append((x, y))
        here = (x, y)
    
    row_label = sorted(routes, key=lambda x : x[0])
    col_label = sorted(routes, key=lambda x : x[1])
    row_length = abs(row_label[0][0]) + abs(row_label[-1][0])
    col_length = abs(col_label[0][1]) + abs(col_label[-1][1])

    if row_length and col_length:
        answers.append(row_length * col_length)
    else:
        answers.append(0)

for ans in answers:
    print(ans)