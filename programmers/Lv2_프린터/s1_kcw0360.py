from collections import deque

def solution(priorities, location):
    q = deque()

    for i in range(len(priorities)):
        if i == location:    # q 에 내가 요청한 것만 True로 표시해서 넣어 주기
            q.append([priorities[i], True])
        else:
            q.append([priorities[i], False])

    answer = 0    # 요청 문서가 몇번째 인지 카운트

    while q:
        temp = q.popleft()
        try:
            for i in q:    # 꺼낸 temp 보다 중요도가 높은 것이 있는지 확인
                if temp[0] < i[0]:    # 중요도가 높은게 존재 한다면
                    q.append(temp)    # 가장 마지막으로 보내기
                    continue    # 다음 인쇄 대기목록 확인
            answer += 1    # 중요도가 높은게 존재하지 않는다면 인쇄
        except:
            continue

        if temp[1]:    # 내가 요청한 인쇄물일 경우 return
            return answer