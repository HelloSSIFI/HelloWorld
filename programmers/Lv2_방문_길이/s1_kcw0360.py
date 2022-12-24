def solution(dirs):
    answer = 0
    direction = {'U': (-1, 0), 'D': (1, 0),  'R': (0, 1), 'L': (0, -1)}    # 명령어
    now = (0, 0)    # 시작 좌표
    visited = set()    # 방문 지점 체크

    for com in dirs:    # 명령어 하나씩 체크
        nxt = (now[0]+direction[com][0], now[1]+direction[com][1])    # 다음 이동 지점
        if -5 <= nxt[0] <= 5 and -5 <= nxt[1] <= 5:    # 좌표 내 존재 여부 확인
            temp = (now, nxt)
            if temp not in visited:    # 현재 지나가려는 길이 지나갔던 길인지 체크
                answer += 1    # 지나간 길이 아닌 경우 answer +1
                visited.add((now, nxt))    # 지나간 길 체크
                visited.add((nxt, now))    # visited에 nxt좌표에서 now로 오는 방향도 체크
            now = nxt
        else:    # 좌표 밖인 경우 다음 명령어 실행
            continue

    return answer