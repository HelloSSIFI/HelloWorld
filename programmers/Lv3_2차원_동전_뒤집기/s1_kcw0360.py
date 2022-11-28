def solution(beginning, target):
    answer = 9876543210
    n = len(beginning)
    m = len(beginning[0])

    flipped = []
    # 미리 원본 배열을 flip시켜서 저장
    for i in range(n):
        flipped.append([])
        for j in range(m):
            if beginning[i][j]:
                flipped[i].append(0)
            else:
                flipped[i].append(1)

    for unit in range(1 << n):
        row_flipped = []
        flip_cnt = 0
        # 행 뒤집기
        for i in range(n):
            comp = 1 << i
            if unit & comp:
                row_flipped.append(flipped[i][:])
                flip_cnt += 1
            else:
                row_flipped.append(beginning[i][:])

        # 열 뒤집기
        for j in range(m):
            temp = []
            check = []

            for i in range(n):
                temp.append(row_flipped[i][j])
                check.append(target[i][j])

            # 현재 column과 target column이 다르면 뒤집기
            if temp != check:
                for i in range(len(row_flipped)):
                    if row_flipped[i][j] == 1:
                        row_flipped[i][j] = 0
                    else:
                        row_flipped[i][j] = 1
                flip_cnt += 1

        # 뒤집은 결과가 target과 같으면 횟수 갱신
        if row_flipped == target:
            answer = min(answer, flip_cnt)

    if answer == 9876543210:
        answer = -1

    return answer