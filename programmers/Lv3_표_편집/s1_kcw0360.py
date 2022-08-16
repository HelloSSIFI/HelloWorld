def solution(n, k, cmd):
    answer = ['O'] * n
    table = [[i-1, i+1] for i in range(n)]    # 현재 idx 앞 뒤 값을 value로 지정
    table[0] = [None, 1]    # 0은 앞, n-1은 뒤가없기 때문에 None으로 표기
    table[n-1] = [n-2, None]
    storage = []
    selection = k

    for i in cmd:
        if i[0] == 'U':    # cmd가 U인 경우 위로이동
            for _ in range(int(i[2:])):    # None이 존재하는 구간때문에 차례대로 하나씩 확인하며 이동
                selection = table[selection][0]    # selection 값이 현재 key값의 이전 값을 선택하며 이동

        elif i[0] == 'D':    # cmd가 아래인 경우 다음 값을 선택하며 이동
            for _ in range(int(i[2:])):
                selection = table[selection][1]

        elif i[0] == 'C':
            answer[selection] = 'X'    # answer에서 삭제표기
            pre, nxt = table[selection]
            storage.append([pre, selection, nxt])    # 삭제 되는 부분 저장

            # selection 값 변경
            if nxt == None:    # 삭제되는 행의 다음 행이 없는 경우
                selection = table[selection][0]    # 이전 값으로 선택
            else:    # 삭제시 다음 행 번호 선택
                selection = table[selection][1]

            # table 값 변경
            if pre == None:    # 가장 첫번째 행인 경우
                table[nxt][0] = None    # 다음 행이 첫번째가 되기 때문에 다음행의 이전 값을 None으로 변경
            elif nxt == None:    # 가장 마지막 행인 경우
                table[pre][1] = None    # 이전 행이 마지막이 되기 때문에 이전행의 다음 값을 None으로 변경
            else:    # 그 외의 경우 앞의 행의 다음 값, 뒤의 행의 이전 값을 서로 이어줌
                table[pre][1] = nxt
                table[nxt][0] = pre

        elif i[0] == 'Z':
            pre, now, nxt = storage.pop()
            answer[now] = 'O'    # 삭제됬던 부분 복구
            if pre == None:    # 복구된 행이 첫번째 행인 경우
                table[nxt][0] = now    # 다음 행의 이전 값을 복구된 행으로 바꿔주기
            elif nxt == None:    # 복구된 행이 마지막 행인 경우
                table[pre][1] = now    # 이전 행의 다음 값을 복구된 행으로 바꿔주기
            else:    # 그 외의 경우 앞의 행의 다음 값, 이전 행의 다음 값을 복구된 값으로 변경
                table[pre][1] = now
                table[nxt][0] = now

    return ''.join(answer)