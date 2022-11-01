def solution(order):
    answer = 0
    stack = []
    idx = 0

    for i in range(1, len(order)+1):    # 1번 상자부터 번호 순대로 확인
        if order[idx] == i:    # 현재 순서와 실어야 하는 상자번호가 같은 경우
            answer += 1    # 트럭에 싣기
            idx += 1    # 상자 번호(idx) +1
            while stack:    # 보조 컨베이어 벨트 위에 있는 것 확인
                if stack[-1] == order[idx]:
                    answer += 1
                    idx += 1
                    stack.pop()    # 보조 컨베이어 벨트에서 제거
                else:
                    break
        else:
            while stack:
                if stack[-1] == order[idx]:
                    answer += 1
                    idx += 1
                    stack.pop()
                else:
                    break
            stack.append(i)

    return answer