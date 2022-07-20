from collections import deque
import heapq
def solution(jobs):
    answer = 0
    jobs.sort(key=lambda x : (x[0], x[1]))                  # 요청 시간 순으로 정렬
    task_q = deque(jobs)

    first_task = task_q.popleft()                           # 가장 처음 실행하는 작업 pop
    disk_q = [(first_task[1], first_task)]                  # (cost, (요청 시간, 작업 시간))
    
    times = []                                              # 작업 별 완료 시간
    total_ms = first_task[0]                                # 실행
    while disk_q:                                           # 디스크가 빌 때까지
        cost, disk = heapq.heappop(disk_q)                  # heapq에서 disk를 pop
        print('disk: ', disk)
        total_ms += cost                                    # 현재 시간에서 현재 disk의 작업 시간 누적
        print('total_ms: ', total_ms)
        times.append(total_ms - disk[0])                    # 작업 완료 시간 append

        while task_q:                                       
            if task_q[0][0] <= total_ms:                    # 다음 task의 요청 시간이 현재 task의 작업 시간 범위 안에 있다면
                task = task_q.popleft()                     # 다음 task를 pop
                heapq.heappush(disk_q, (task[1], task))     # disk_q는 작업 시간의 최소값을 유지하는 최소힙
            else:
                break
        
        if not disk_q and task_q:                               # disk_q가 비었으나 task_q가 남아있는 경우
            next_task = task_q.popleft()                        # 곧바로 작업 시작
            heapq.heappush(disk_q, (next_task[1], next_task))   # disk_q에 삽입
            total_ms = next_task[0]                             # 새로 실행하는 task의 요청 시간까지 jump
    
    answer = sum(times) // len(jobs)
    print(times) 
    return answer

print(solution([[0, 5], [2, 10], [10000, 2]]))
