def operate(mat, p):
    # 행방향 if p else 열방향
    # 새로 반환할 배열
    new_mat = []
    # 가장 큰 행 또는 열의 길이
    n = 0
    # 현재 행 또는 열
    for row in mat:
        # (숫자, 등장 횟수) 를 담을 배열
        line = []

        for num in set(row):
            # 0은 continue
            if num == 0:continue

            # 등장 횟수
            cnt = row.count(num)
            # 숫자, 등장횟수 append
            line.append((num, cnt))
        # 등장 횟수 우선, 다음 숫자 우선으로 정렬
        line.sort(key=lambda x: [x[1], x[0]])

        # 새로 반환할 배열에 추가할 행 또는 열
        new_row = []

        # 숫자와 등장 횟수를 꺼내면서
        for num, cnt in line:
            # 현재 행 또는 열에 extend
            new_row += [num, cnt]

        # 다 추가 했으면 append
        new_mat.append(new_row)

        # 최대 행 또는 열 길이 갱신
        n = max(n, len(new_row))

    # 새 반환할 배열을 돌면서 최대 길이에 맞게 0 추가
    for row in new_mat:
        row += [0]*(n-len(row))
        if len(row) > 100: row = row[:100]

    # 열연산이었으면 새로로 전치해서 return
    return new_mat if p else list(zip(*new_mat))


r, c, k = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(3)]

time = 0
r -= 1
c -= 1
while time <= 100:
    # 배열에 위치에 k 값이면 break
    if r < len(field) and c < len(field[0]) and field[r][c] == k:
        break

    # R연산
    if len(field) >= len(field[0]):
        field = operate(field, 1)
    # C연산
    else:
        field = operate(list(zip(*field)), 0)

    # 시간 추가
    time += 1

print(time if time <= 100 else -1)