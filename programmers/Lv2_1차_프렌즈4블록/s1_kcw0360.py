answer = 0
game = []

def block(m, n):
    global answer
    del_block = set()    # 지워야할 블록 좌표 저장(중복된 좌표 없애기 위해 set으로 설정)
    res = True    # 블록을 지울 수 있을 때 True

    # 체크 해야 할 위치 - 현 위치에서 2x2가 되는 곳만 체크 하도록 함
    dy = [0, 1, 1]
    dx = [1, 0, 1]

    for i in range(m-1):
        for j in range(n-1):
            temp = set()    # 현 위치와 같은 블록인경우 좌표 임시저장
            if game[i][j]:
                for k in range(3):    # 2x2 체크
                    y = i + dy[k]
                    x = j + dx[k]

                    if game[i][j] == game[y][x]:    # 현 위치와 같은 블록인 경우 temp에 저장
                        temp.add((y, x))
            if len(temp) == 3:    # 체크해야할 위치에 모두 같은 블록인 경우
                temp.add((i, j))    # 빠져 있는 현위치도 temp에 저장
                del_block |= temp    # 그리고 지워야할 블록 좌표에 합집합으로 좌표 추가

    if del_block:    # 지워야할 좌표가 존재하는 경우
        answer += len(del_block)    # answer에 지워야할 블록 갯수 더해주기
        for i in del_block:    # 블록 삭제
            game[i[0]][i[1]] = 0

        for j in range(n):    # 삭제한 블록 떨어뜨리기
            temp = []
            for i in range(m):
                if game[i][j]:
                    temp.append(game[i][j])
            length = m - len(temp)
            temp = ([0]*length) + temp
            for i in range(m):
                game[i][j] = temp[i]
    else:    # 지워야할 블록이 없다면 결과값을 False로 리턴
        res = False

    return res

def solution(m, n, board):
    for i in board:    # 입력값(board)의 문자열을 분리한 리스트로 만들기
        game.append(list(i))

    while True:    # 더 이상 지워질 블록이 없어질 때 까지 반복진행
        temp = block(m, n)    # 블록 지우기
        if temp == False:    # 블록 지운 후 출력 값이 False인 경우 더 이상 지워질 블록이 없다는 것
            break    # while문 나가기

    return answer
