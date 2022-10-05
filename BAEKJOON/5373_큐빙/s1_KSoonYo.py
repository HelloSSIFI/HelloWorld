import sys
from collections import deque

input = sys.stdin.readline


def rotate(cube, development, direction):
    target = development['vertical'][1] # 현재 정면

    # 전개도 상에서 현재 타겟의 면들과 인접한 이웃들(위, 왼 아, 오)
    neighbors = [development['vertical'][0], development['horizon'][0], development['vertical'][2], development['horizon'][2]]

    # 위, 왼, 가운데, 오, 아래 통합 행렬 구현 뒤에 시계 방향 or 반시계 방향 회전
    
    up = [[0] + cube[neighbors[0]][2][:] + [0]]     # 윗 줄
    middle = []
    down = [[0] + cube[neighbors[2]][0][:] + [0]]   # 아랫 줄

    for row in range(3):
        l = cube[neighbors[1]][row]
        m = cube[target][row]
        r = cube[neighbors[3]][row]
        middle.append([l[2], m[0], m[1], m[2], r[0]])

    matrix = up + middle + down

    if direction == '+':
        # 시계 방향
        matrix = list(map(list, zip(*matrix[::-1])))
    else:
        #반시계 방향
        matrix = list(map(list, zip(*matrix)))[::-1]


    cube[neighbors[0]][2] = [i for i in matrix[0][1:4]]
    
    for row in range(3):
        cube[neighbors[1]][row][2], cube[target][row][0], cube[target][row][1], cube[target][row][2], cube[neighbors[3]][row][0] = matrix[row + 1][:]

    cube[neighbors[2]][0] = [i for i in matrix[4][1:4]]



# 시계 or 반시계 방향으로 회전하려는 면을 큐브를 돌려서 정면에 위치시키는 함수
def position(cube, development, target):
    # horizon 방향으로 회전하는 경우 -> B면의 열을 거꾸로, 타겟을 정면에 위치시킨 뒤에 vertical[1]을 타겟으로 변환 [3]을 타겟의 맞은편으로 변환, 큐브 회전 뒤에 vertical 위쪽과 아래쪽 면을 회전 방향과 횟수에 따라 테두리 회전 
    # vertical 방향으로 회전할 경우 -> 타겟을 정면에 위치시킨 뒤에 horizion[1]을 타겟으로 변환 [3]을 타겟의 맞은편으로 변환, 큐브 회전 뒤에 horizon 왼쪽과 오른쪽 면을 회전 방향과 횟수에 따라 테두리 회전
    
    # vertical: [0번째 위쪽, 1번째: 정면, 2번째: 아래쪽, 3번째: 맞은편]
    # horizon: [0번재: 왼쪽, 1번째: 정면, 2번째: 오른쪽, 3번째: 맞은편]


    # 1) 타겟을 정면에 위치시키기
    if target == development['vertical'][1]:
        # 이미 정면에 위치한다면 return
        return

    direction = ''    
    sub_direction = ''
    n = 0
    if target in development['vertical']:
        direction = 'vertical'
        if development['vertical'][0] == target:
            sub_direction = 'R'
            n = 1
        else:
            sub_direction = 'L'
            n = development['vertical'].index(target) - 1
    else:
        # 수평으로 큐브를 돌릴 경우, F의 맞은편 B 면의 열을 거꾸로 해야 함(좌, 우 면과 맞닿은 면이 반대이기 때문)
        # B면을 정면에 위치시킬 때는 수직으로 큐브를 돌리는 경우이며 순서가 처음 그대로여야 하기 때문에 수평으로 돌릴 때만 열을 거꾸로 해준다. 
        cube['B'] = list(map(lambda x : x[::-1], cube['B']))[::-1]

        direction = 'horizon'
        if development['horizon'][0] == target:
            sub_direction = 'R'
            n = 1
        else:
            sub_direction = 'L'
            n = development['horizon'].index(target) - 1

    k = 0
    while k < n:
        if sub_direction == 'R':
            temp = development[direction].pop()
            development[direction].appendleft(temp)

        else:
            temp = development[direction].popleft()
            development[direction].append(temp)
        k += 1
    

    across = {
        'L' : 'R', 'R' : 'L', 
        'F' : 'B', 'B' : 'F',
        'U' : 'D', 'D' : 'U'
    }


    if direction == 'vertical':
        development['horizon'][1] = target
        development['horizon'][3] = across[target]
        
    else:
        development['vertical'][1] = target
        development['vertical'][3] = across[target]
    

    # 2) 맞닿은 면 회전 & 큐브 업데이트
    rotate_group = 'vertical' if direction == 'horizon' else 'horizon'
    if sub_direction == 'R':
        # vertical 위쪽 or horizon 오른쪽은 반시계 방향으로 90도 회전, vertical 아래쪽 or horizon 왼쪽은 시계 방향으로 90도 회전
        clock_wise = development[rotate_group][2] if rotate_group == 'vertical' else development[rotate_group][0]
        counter_clock = development[rotate_group][0] if rotate_group == 'vertical' else development[rotate_group][2]
    else:
        # 위와 반대
        clock_wise = development[rotate_group][0] if rotate_group == 'vertical' else development[rotate_group][2]
        counter_clock = development[rotate_group][2] if rotate_group == 'vertical' else development[rotate_group][0]

   
    while n > 0:
        cube[clock_wise] = list(map(list, zip(*cube[clock_wise][::-1])))
        cube[counter_clock] = list(map(list, zip(*cube[counter_clock])))[::-1]
        n -= 1

for _ in range(int(input())):
    n = int(input())
    commands = input().strip().split()

    cube = {
        'U' : [['w'] * 3 for _ in range(3)],
        'D' : [['y'] * 3 for _ in range(3)],
        'F' : [['r'] * 3 for _ in range(3)],
        'B' : [['o'] * 3 for _ in range(3)],
        'L' : [['g'] * 3 for _ in range(3)],
        'R' : [['b'] * 3 for _ in range(3)]
    }


    for command in commands:
        target, direction = command[0], command[1]

        # 전개도
        # vertical과 horizon의 1번째 인덱스가 정면에 위치한 면
        # vertical: [0번째 위쪽, 1번째: 정면, 2번째: 아래쪽, 3번째: 맞은편]
        # horizon: [0번재: 왼쪽, 1번째: 정면, 2번째: 오른쪽, 3번째: 맞은편]
        development = {
            'vertical' : deque(['U', 'F', 'D', 'B']),
            'horizon' : deque(['L', 'F', 'R', 'B']),
        }

        position(cube, development, target)                 # 정면 위치시키기

        rotate(cube, development, direction)                # 회전
    
        position(cube, development, target='F')             # 원상복구

    for row in cube['U']:
        print(''.join(row))

