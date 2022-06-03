H, W = map(int, input().split())
numbers = list(map(int, input().split()))

block = [[0]*W for _ in range(H)]    # 블록 쌓을 공간, 블록이 있다면 1, 없으면 0

for i in range(W):    # 블록을 상단부터 채워 나간다. 문제에 예시 그림이 상하 반전이라고 생각하면 될 것
    for j in range(numbers[i]):
        block[j][i] = 1

result = 0    # 결과값

for i in range(H):    # 첫 째줄이 바닥이기 때문에 순서대로 리스트를 확인
    wall = 0    # 빗물이 고이기 위한 벽이 되는 것을 체크
    temp = 0    # 빗물 임시저장
    for j in range(W):
        if wall == 0 and block[i][j] == 1:    # 벽이 아직 없고, 현 위치에 블록이 있다면 현 위치가 기둥이 되는 블록이므로 wall에 1로 표시
            wall = 1
        elif wall == 1 and block[i][j] == 0:    # 벽이 있고, 0이 있다면 빗물이 고인다고 생각하여 temp에 빗물 저장
            temp += 1
        elif wall == 1 and block[i][j] == 1:    # 벽이 있는 상태에서 또 다른 벽이 있다면 물이 고일 수 있다는 것
            result += temp    # 따라서 temp에 저장된 빗물을 result에 더한 후 초기화
            temp = 0

print(result)



