import heapq

def solution(jobs):
    answer = 0
    N = len(jobs)
    jobs.sort(reverse=True)
    waiting = []                                        # 대기중인 작업
    sec = 0                                             # 현재 시간
    while jobs or waiting:                              # 남은 작업이 남은동안 반복
        if not waiting:                                 # 대기열에 없으면
            s, p = jobs.pop()                           # 현재 시간을 가장 빠른 작업으로 맞춘 후
            sec = s                                     # 대기열에 가장 빠른 작업을 넣어줌
            heapq.heappush(waiting, [p, s])
        
        p, s = heapq.heappop(waiting)                   # 대기열에서 소요시간이 가장 적은것을 꺼내줌
        sec += p                                        # 시간을 소요시간만큼 더해줌
        answer += sec - s                               # 이 작업의 요청부터 종료까지 시간을 answer에 더해줌
        while jobs and jobs[-1][0] <= sec:              # 현재 시간에 맞춰 대기열에 작업을 넣어줌
            heapq.heappush(waiting, jobs.pop()[::-1])
    return answer // N


# print(solution([[0, 3], [1, 9], [2, 6]]))
