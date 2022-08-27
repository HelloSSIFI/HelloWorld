import sys
input = sys.stdin.readline


T = int(input())

answer = []
for _ in range(T):
    command = list(input())
    check1 = [0, 0]    # 상 하
    check2 = [0, 0]    # 좌 우
    direction = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}    # 상 우 하 좌
    start = [0, 0]    # 시작점
    d = 0    # 바라보는 방향


    def check():    # 현재 위치가 가장 끝에 있는 경우 인지 체크
        if check1[0] > start[0]:    # 북쪽 좌표 체크
            check1[0] = start[0]
        if check1[1] < start[0]:    # 남쪽 좌표 체크
            check1[1] = start[0]
        if check2[0] > start[1]:    # 서쪽 좌표 체크
            check2[0] = start[1]
        if check2[1] < start[1]:    # 동쪽 좌표 체크
            check2[1] = start[1]


    for com in command:
        if com == 'R':    # 우향우
            d = (d+1) % 4
        elif com == 'L':    # 좌향좌
            d = (d-1) % 4
        elif com == 'F':    # 한 칸 전진
            start[0] += direction[d][0]
            start[1] += direction[d][1]
            check()
        elif com == 'B':    # 백스텝
            start[0] += direction[d][0] * -1
            start[1] += direction[d][1] * -1
            check()

    answer.append('{}\n'.format((check1[1]-check1[0])*(check2[1]-check2[0])))    # 사각형 넓이 구하기

print(''.join(answer))