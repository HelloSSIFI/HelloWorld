def solution(line):
    point = set()
    for i in range(len(line) - 1):
        A, B, E = line[i]
        for j in range(i + 1, len(line)):
            C, D, F = line[j]

            if A * D == B * C:
                continue                                                                        # 두 선이 평행하거나
            if (B * F - E * D) % (A * D - B * C) or (E * C - A * F) % (A * D - B * C):          # 교점이 정수가 아니면
                continue                                                                        # 다음반복

            x = (B * F - E * D) // (A * D - B * C)                                              # 교점을 계산
            y = (E * C - A * F) // (A * D - B * C)

            point.add((-y, x))                                                                  # r, c에 맞게 넣어줌

    min_r = min_c = float('inf')
    max_r = max_c = float('-inf')
    for r, c in point:                                                                          # r, c 중 최소값과 최대값을 찾아줌
        min_r = min(min_r, r)                                                                   # 빈공간을 없애기 위해 모든 좌표를 최소값으로 빼줄 예정
        min_c = min(min_c, c)
        max_r = max(max_r, r)
        max_c = max(max_c, c)

    max_r = max_r - min_r + 1                                                                   # 최대값에서도 각각 최소값을 빼준 값이 각각 행과 열의 크기
    max_c = max_c - min_c + 1
    answer = [['.'] * max_c for _ in range(max_r)]                                              # 구해진 최대값으로 .으로 된 행열을 만들어줌
    for r, c in point:
        answer[r - min_r][c - min_c] = '*'                                                      # 교점 좌표를 *로 바꿔주고
    for i in range(len(answer)):                                                                # 한 줄의 여러 문자를 문자열로 바꿔서 저장
        answer[i] = ''.join(answer[i])
    return answer


# print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
