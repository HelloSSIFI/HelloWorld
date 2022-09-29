import sys
input = sys.stdin.readline


def c_w(d):                                             # 큐브의 d방향 면을 시계방향으로 90도 회전하는 함수
    cube[d] = list(map(list, zip(*cube[d][::-1])))


def c_c_w(d):                                           # 큐브의 d방향 면을 반시계방향으로 90도 회전하는 함수
    cube[d] = list(map(list, zip(*cube[d])))[::-1]


def rot(target, r):                                     # 큐브 동작을 실행하는 함수
    s = 4
    d = -1
    if r == '+':                                        # 해당 면을 +-에 따라 시계 혹은 반시계로 돌려주고
        c_w(target[0])                                  # 돌릴때 영향을 받는 면을 각각 바꿔줌
    elif r == '-':                                      # 이 때 영향을 받는 줄을 모두 해당 면의 맨 윗줄에 고정시켜서
        s = 1                                           # 각각의 면의 윗줄만 바꿔줌
        d = 1                                           # 반시계방향일 때는 시계방향일 때의 역순
        c_c_w(target[0])

    cube[target[s]][0], cube[target[s + d]][0], cube[target[s + d * 2]][0], cube[target[s + d * 3]][0] = cube[target[s + d]][0], cube[target[s + d * 2]][0], cube[target[s + d * 3]][0], cube[target[s]][0]


answer = []
for _ in range(int(input())):
    n = int(input())
    com = list(input().split())
    cube = {'U': [['w'] * 3 for i in range(3)], 'D': [['y'] * 3 for i in range(3)], 'F': [['r'] * 3 for i in range(3)],
            'B': [['o'] * 3 for i in range(3)], 'L': [['g'] * 3 for i in range(3)], 'R': [['b'] * 3 for i in range(3)]}
    conn = {'U': ['U', 'B', 'R', 'F', 'L'], 'D': ['D', 'F', 'R', 'B', 'L'],
            'F': ['F', 'U', 'R', 'D', 'L'], 'B': ['B', 'D', 'R', 'U', 'L'],
            'L': ['L', 'U', 'F', 'D', 'B'], 'R': ['R', 'U', 'B', 'D', 'F']}
    cnt = {'U': 0, 'B': 1, 'D': 2, 'F': 3}      # cube, conn, cnt 초기값 설정

    for c in com:
        d, r = c                                # 돌리는 면을 key로 영향을 받는 면을 모두 conn에 저장
        if d in cnt:                            # 영향을 받는 면의 첫번째 요소는 돌리는 면으로 시계 또는 반시계로 회전할 예정
            for i in range(cnt[d]):             # 나머지 4면은 영향받는 줄을 맨 윗줄로 올려줄 예정
                c_c_w('R')                      # 돌리는 면이 U B D F 중 하나일 경우
                c_w('L')                        # 초기 L과 R의 윗줄은 U와 맞닿는 줄이며 회전축에 따라 각각을 돌려주어야 함
            for i in range(2):                  # 돌려주는 회수는 cnt에 저장
                c_w(conn[d][1])                 # 그 외 자신의 윗면은 180도 회전해야 윗줄이 영향이 받는 줄이 됨

        else:                                   # 돌리는 면이 L R 일 경우
            for target in conn[d][1:]:          # 영향을 받는 면은 U B D F 이며
                if d == 'R':                    # R일 경우 반시계, L일 경우 시계로 돌려주면
                    c_c_w(target)               # 영향을 받는 면이 위로 올라감
                else:
                    c_w(target)

        rot(conn[d], r)                         # 큐브를 돌려주고

        if d in cnt:                            # 위에서 돌린 것들을 원상 복귀
            for i in range(cnt[d]):
                c_w('R')
                c_c_w('L')
            for i in range(2):
                c_w(conn[d][1])

        else:
            for target in conn[d][1:]:
                if d == 'R':
                    c_w(target)
                else:
                    c_c_w(target)

    for i in range(3):
        answer.append(''.join(cube['U'][i]))
        answer.append('\n')

print(''.join(answer))
