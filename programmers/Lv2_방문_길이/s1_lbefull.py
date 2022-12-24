def solution(dirs):
    answer = set()
    mv = {'U': [0, 1], 'D': [0, -1], 'R': [1, 0], 'L': [-1, 0]}     # 명령어별 이동을 저장
    x = y = 0                                                       # 초기 위치
    for d in dirs:
        nx = x + mv[d][0]                                           # 명령어대로 이동한 위치를 nx, ny로 저장
        ny = y + mv[d][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:                         # nx, ny가 좌표를 벗어나지 않으면
            if d in 'UR':                                           # 좌표가 오름차순으로 작은 쪽에서 큰 쪽으로 가는 순서대로 튜플을 만들어서
                answer.add((x, y, nx, ny))                          # answer에 추가
            else:
                answer.add((nx, ny, x, y))
            x, y = nx, ny                                           # 새로운 좌표를 가지고 다음 명령어 반복

    return len(answer)


# print(solution('ULURRDLLU'))
