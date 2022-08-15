def solution(n, k, cmd):
    answer = ['O'] * n
    deleted = [0] * n
    stack = []
    linked = [[0, 0] for _ in range(n)]
    for i in range(n):                          # 현재 테이블의 이전 값과 다음 값의 인덱스를 연결
        linked[i][0] = i - 1
        linked[i][1] = i + 1

    for c in cmd:                               # 명령 순회
        com = c.split(' ')
        if len(com) > 1:                        # 이동명령일 경우
            d = 1                               # 위쪽인지 아래쪽인지 판별하여 d를 결정
            if com[0] == 'U':
                d = 0
            cnt = int(com[1])                   # 명령된 숫자(cnt) 만큼
            for i in range(cnt):                # k에서 인덱스를 이동
                k = linked[k][d]

        else:
            if com[0] == 'C':                   # 제거 명령일 경우
                l = linked[k][0]                # 현재 k번 자료의 왼쪽과 오른쪽 인덱스를 각각 l, r로 저장
                r = linked[k][1]                # k를 제거 표시해주고
                deleted[k] = 1
                if l > -1:                      # 인덱스 범위 내에서
                    linked[l][1] = r            # l과 r을 서로 연결해주고
                if r < n:
                    linked[r][0] = l
                stack.append(k)                 # 스택에 k를 넣어줌
                k = r                           # 제거 후 바라보는 인덱스를 k의 오른쪽인 r로 변경해주고
                if k == n:                      # 만약 이 값이 인덱스를 초과하면 l로 변경
                    k = l
            else:                               # 복구 명령일 경우
                num = stack.pop()               # 제거된 값들중 최신 인덱스를 num으로 가져옴
                l = linked[num][0]              # 해당 인덱스에 저장된 왼쪽, 오른쪽 인덱스를 각각 l, r로 가져옴
                r = linked[num][1]              # 해당 테이블을 다시 복구 표시
                deleted[num] = 0
                while r < n and deleted[r]:     # 인덱스 범위 내에서 왼쪽, 오른쪽 테이블 중 제거되지 않은
                    r = linked[r][1]            # 가장 가까운 인덱스를 찾아줌
                while l > -1 and deleted[l]:    # num의 왼쪽, 오른쪽 인덱스 값을 갱신해주고
                    l = linked[l][0]            # 해당 값들이 인덱스 범위 내에 있을 경우 해당값을의 각각 오른쪽, 왼쪽 값을 갱신
                linked[num][0] = l
                linked[num][1] = r
                if l > -1:
                    linked[l][1] = num
                if r < n:
                    linked[r][0] = num

    while stack:                                # 명령이 끝난 후 stack에 남아있는 값들이 제거된 인덱스들이므로
        answer[stack.pop()] = 'X'               # 해당 인덱스를 X표시
    return ''.join(answer)


# print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
