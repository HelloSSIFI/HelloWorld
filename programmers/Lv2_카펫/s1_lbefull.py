def solution(brown, yellow):
    y = 3                                       # y를 최소값인 3으로 초기화
    x = brown // 2 - y + 2                      # x를 y와 brown에 맞게 값 설정
    while x >= y:                               # x가 y보다 크거나 같은동안 반복
        if (x - 2) * (y - 2) == yellow:         # 안쪽 넓이가 yellow가 된다면 반복종료
            break
        x -= 1                                  # 아니라면 가로길이-1, 세로길이+1
        y += 1
    return [x, y]
