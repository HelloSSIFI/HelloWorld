def solution(brown, yellow):
    y_list = []    # 노란색 [세로, 가로]
    if yellow == 1:    # 노란색이 1개인 경우
        y_list.append([1, 1])
    else:
        for i in range(1, yellow//2 + 1):    # 노란색 절반까지 확인
            a, b = divmod(yellow, i)    # 몫과 나머지 확인
            if b == 0:    # 나머지가 없이 나누어 떨어지는 경우 노란색의 가로, 세로가 될 수 있다.
                y_list.append([i, a])    # 가로가 더 길기 때문에 a가 가로 i가 세로 값

    total = brown + yellow    # 총 격자 수
    for y, x in y_list:    # 노란색 격자의 가로, 세로가 될 수 있는 것들을 차례대로 확인
        if total == (y+2) * (x+2):    # 갈색 격자가 노란색을 감싸고 있기 때문에 가로, 세로 길이가 각각 2씩 더 크다.
            return [x+2, y+2]    # 곱이 전체 격자 수와 같다면 정답으로 리턴