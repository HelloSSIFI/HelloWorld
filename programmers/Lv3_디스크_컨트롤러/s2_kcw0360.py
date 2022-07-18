import heapq
from collections import deque

def solution(jobs):
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    q = []
    heapq.heappush(q, tasks.popleft())
    current_time, total_response_time = 0, 0    # 현재 작업 중인 시간, 모든 작업의 요청부터 종료까지 시간의 합

    while len(q):
        dur, arr = heapq.heappop(q)    # dur: 작업의 소요시간, arr: 작업이 요청되는 시점
        current_time = max(current_time + dur, arr + dur)    # 작업이 이루어진 후 현재 시간은 (현재 시간 + 작업의 소요시간), (요청시간 + 작업의 소요시간) 중 큰 값으로 채택
        total_response_time += current_time - arr    # 요청 ~ 완료 까지 시간 누적

        while len(tasks) > 0 and tasks[0][1] <= current_time:    # 작업이 남아 있고, 남아있는 작업 중 가장 빠른 것의 요청시간이 지나간 경우
            heapq.heappush(q, tasks.popleft())    # 힙에 작업 추가

        if len(tasks) > 0 and len(q) == 0:    # 작업이 남아 있고, 힙에 남아 있는 작업이 없을 때(작업 요청 시간이 현재 시간 이후에 존재할 경우)
            heapq.heappush(q, tasks.popleft())    # 힙에 작업 추가

    return total_response_time // len(jobs)