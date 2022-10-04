import sys
input = sys.stdin.readline


T = int(input())

for _ in range(T):
    cnt = int(input())    # 돌리는 횟수
    commands = input().split()    # 돌리는 면 + 방향(시계, 반시계)
    up = [['w']*3 for _ in range(3)]    # 윗 면
    down = [['y']*3 for _ in range(3)]    # 아랫 면
    front = [['r']*3 for _ in range(3)]    # 앞 면
    back = [['o']*3 for _ in range(3)]    # 뒷 면
    left = [['g']*3 for _ in range(3)]    # 왼쪽 면
    right = [['b']*3 for _ in range(3)]    # 오른쪽 면

    for com in commands:
        if com[1] == '+':
            if com[0] == 'U':
                up[0][0], up[0][1], up[0][2], up[1][0], up[1][2], up[2][0], up[2][1], up[2][2] = up[2][0], up[1][0], up[0][0], up[2][1], up[0][1], up[2][2], up[1][2], up[0][2]
                front[0][0], front[0][1], front[0][2], right[0][0], right[0][1], right[0][2], back[0][0], back[0][1], back[0][2], left[0][0], left[0][1], left[0][2] = right[0][0], right[0][1], right[0][2], back[0][0], back[0][1], back[0][2], left[0][0], left[0][1], left[0][2], front[0][0], front[0][1], front[0][2]
            elif com[0] == 'D':
                down[0][0], down[0][1], down[0][2], down[1][0], down[1][2], down[2][0], down[2][1], down[2][2] = down[2][0], down[1][0], down[0][0], down[2][1], down[0][1], down[2][2], down[1][2], down[0][2]
                front[2][0], front[2][1], front[2][2], right[2][0], right[2][1], right[2][2], back[2][0], back[2][1], back[2][2], left[2][0], left[2][1], left[2][2] = left[2][0], left[2][1], left[2][2], front[2][0], front[2][1], front[2][2], right[2][0], right[2][1], right[2][2], back[2][0], back[2][1], back[2][2]
            elif com[0] == 'F':
                front[0][0], front[0][1], front[0][2], front[1][0], front[1][2], front[2][0], front[2][1], front[2][2] = front[2][0], front[1][0], front[0][0], front[2][1], front[0][1], front[2][2], front[1][2], front[0][2]
                right[0][0], right[1][0], right[2][0], up[2][0], up[2][1], up[2][2], left[2][2], left[1][2], left[0][2], down[2][0], down[2][1], down[2][2] = up[2][0], up[2][1], up[2][2], left[2][2], left[1][2], left[0][2], down[2][0], down[2][1], down[2][2], right[0][0], right[1][0], right[2][0]
            elif com[0] == 'B':
                back[0][0], back[0][1], back[0][2], back[1][0], back[1][2], back[2][0], back[2][1], back[2][2] = back[2][0], back[1][0], back[0][0], back[2][1], back[0][1], back[2][2], back[1][2], back[0][2]
                up[0][0], up[0][1], up[0][2], right[0][2], right[1][2], right[2][2], down[0][0], down[0][1], down[0][2], left[2][0], left[1][0], left[0][0] = right[0][2], right[1][2], right[2][2], down[0][0], down[0][1], down[0][2], left[2][0], left[1][0], left[0][0], up[0][0], up[0][1], up[0][2]
            elif com[0] == 'L':
                left[0][0], left[0][1], left[0][2], left[1][0], left[1][2], left[2][0], left[2][1], left[2][2] = left[2][0], left[1][0], left[0][0], left[2][1], left[0][1], left[2][2], left[1][2], left[0][2]
                front[0][0], front[1][0], front[2][0], down[2][2], down[1][2], down[0][2], back[2][2], back[1][2], back[0][2], up[0][0], up[1][0], up[2][0] = up[0][0], up[1][0], up[2][0], front[0][0], front[1][0], front[2][0], down[2][2], down[1][2], down[0][2], back[2][2], back[1][2], back[0][2]
            else:
                right[0][0], right[0][1], right[0][2], right[1][0], right[1][2], right[2][0], right[2][1], right[2][2] = right[2][0], right[1][0], right[0][0], right[2][1], right[0][1], right[2][2], right[1][2], right[0][2]
                up[0][2], up[1][2], up[2][2], front[0][2], front[1][2], front[2][2], down[2][0], down[1][0], down[0][0], back[2][0], back[1][0], back[0][0] = front[0][2], front[1][2], front[2][2], down[2][0], down[1][0], down[0][0], back[2][0], back[1][0], back[0][0], up[0][2], up[1][2], up[2][2]
        else:
            if com[0] == 'U':
                up[0][0], up[0][1], up[0][2], up[1][0], up[1][2], up[2][0], up[2][1], up[2][2] = up[0][2], up[1][2], up[2][2], up[0][1], up[2][1], up[0][0], up[1][0], up[2][0]
                front[0][0], front[0][1], front[0][2], right[0][0], right[0][1], right[0][2], back[0][0], back[0][1], back[0][2], left[0][0], left[0][1], left[0][2] = left[0][0], left[0][1], left[0][2], front[0][0], front[0][1], front[0][2], right[0][0], right[0][1], right[0][2], back[0][0], back[0][1], back[0][2]
            elif com[0] == 'D':
                down[0][0], down[0][1], down[0][2], down[1][0], down[1][2], down[2][0], down[2][1], down[2][2] = down[0][2], down[1][2], down[2][2], down[0][1], down[2][1], down[0][0], down[1][0], down[2][0]
                front[2][0], front[2][1], front[2][2], right[2][0], right[2][1], right[2][2], back[2][0], back[2][1], back[2][2], left[2][0], left[2][1], left[2][2] = right[2][0], right[2][1], right[2][2], back[2][0], back[2][1], back[2][2], left[2][0], left[2][1], left[2][2], front[2][0], front[2][1], front[2][2]
            elif com[0] == 'F':
                front[0][0], front[0][1], front[0][2], front[1][0], front[1][2], front[2][0], front[2][1], front[2][2] = front[0][2], front[1][2], front[2][2], front[0][1], front[2][1], front[0][0], front[1][0], front[2][0]
                right[0][0], right[1][0], right[2][0], up[2][0], up[2][1], up[2][2], left[2][2], left[1][2], left[0][2], down[2][0], down[2][1], down[2][2] = down[2][0], down[2][1], down[2][2], right[0][0], right[1][0], right[2][0], up[2][0], up[2][1], up[2][2], left[2][2], left[1][2], left[0][2]
            elif com[0] == 'B':
                back[0][0], back[0][1], back[0][2], back[1][0], back[1][2], back[2][0], back[2][1], back[2][2] = back[0][2], back[1][2], back[2][2], back[0][1], back[2][1], back[0][0], back[1][0], back[2][0]
                right[0][2], right[1][2], right[2][2], down[0][0], down[0][1], down[0][2], left[2][0], left[1][0], left[0][0], up[0][0], up[0][1], up[0][2] = up[0][0], up[0][1], up[0][2], right[0][2], right[1][2], right[2][2], down[0][0], down[0][1], down[0][2], left[2][0], left[1][0], left[0][0]
            elif com[0] == 'L':
                left[0][0], left[0][1], left[0][2], left[1][0], left[1][2], left[2][0], left[2][1], left[2][2] = left[0][2], left[1][2], left[2][2], left[0][1], left[2][1], left[0][0], left[1][0], left[2][0]
                up[0][0], up[1][0], up[2][0], front[0][0], front[1][0], front[2][0], down[2][2], down[1][2], down[0][2], back[2][2], back[1][2], back[0][2] = front[0][0], front[1][0], front[2][0], down[2][2], down[1][2], down[0][2], back[2][2], back[1][2], back[0][2], up[0][0], up[1][0], up[2][0]
            else:
                right[0][0], right[0][1], right[0][2], right[1][0], right[1][2], right[2][0], right[2][1], right[2][2] = right[0][2], right[1][2], right[2][2], right[0][1], right[2][1], right[0][0], right[1][0], right[2][0]
                front[0][2], front[1][2], front[2][2], up[0][2], up[1][2], up[2][2], back[2][0], back[1][0], back[0][0], down[2][0], down[1][0], down[0][0] = up[0][2], up[1][2], up[2][2], back[2][0], back[1][0], back[0][0], down[2][0], down[1][0], down[0][0], front[0][2], front[1][2], front[2][2]

    for row in up:
        print(''.join(row))