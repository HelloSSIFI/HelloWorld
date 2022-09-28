import sys, heapq
input = sys.stdin.readline


N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]
schedule.sort(key=lambda x: (x[0], x[1]))           # 수업시간을 시작시간 기준 오름차순 정렬
answer = 1
heap = []                                           # 종료시간을 기준으로 힙을 생성하고 첫번째 수업을 넣어줌
for i in range(N):
    s, e = schedule[i]
    while heap and s >= heap[0][0]:                 # 힙에서 현재 수업의 시작시간보다 종료시간이 작은 것들을 모두 빼줌
        heapq.heappop(heap)
    heapq.heappush(heap, [e, s])                    # 현재 수업을 힙에 넣어줌
    answer = max(answer, len(heap))                 # 힙의 길이가 answer보다 크다면 갱신
print(answer)
