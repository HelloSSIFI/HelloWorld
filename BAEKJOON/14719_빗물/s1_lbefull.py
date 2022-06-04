def check(r, c, d, w):                  # 현재 위치 왼쪽 또는 오른쪽에 벽이 있는지 체크
    for i in range(c + d, w, d):        # r, c : 현재 인덱스, d : 왼쪽 or 오른쪽, w : 왼쪽 or 오른쪽 범위
        if block[i] >= r:               # 벽이 있으면 True 없으면 False
            return True
    return False


H, W = map(int, input().split())
block = list(map(int, input().split()))

result = 0
for c in range(W):                      # 왼쪽부터 찾아봄
    for r in range(H, 0, -1):           # 위부터 찾아서 위에 물이 고일 수 있으면 아래도 다 고일 수 있음
        if block[c] >= r:               # r이 벽높이 이하가 되면 현재열은 물이 고일 수 없음
            break

        if check(r, c, -1, -1) and check(r, c, 1, W):       # 양 옆에 고일 수 있는지 체크
            result += r - block[c]                          # 고일 수 있다면 아래공간 포함 result에 추가
            break

print(result)
