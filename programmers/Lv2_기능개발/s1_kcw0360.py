from collections import deque

def solution(progresses, speeds):
    answer = []
    q_pr = deque()
    q_sp = deque()
    q_pr.extend(progresses)
    q_sp.extend(speeds)

    while q_pr:
        # 배포전 그 날 작업수행
        for i in range(len(q_pr)):
            q_pr[i] += q_sp[i]
        # 배포가능 확인
        cnt = 0 # 배포가능한 기능 카운트
        while q_pr:
            if q_pr[0] >= 100:
                q_pr.popleft()
                q_sp.popleft()
                cnt += 1
            else:
                break
        if cnt:
            answer.append(cnt)
    return answer