import heapq, sys
input = sys.stdin.readline


N = int(input())

time_table = [list(map(int, input().split())) for _ in range(N)]
time_table.sort()    # 수업시작시간이 빠른 순서대로 정렬

class_room = []    # 강의실
heapq.heappush(class_room, time_table[0][1])    # 첫 수업(종료시간 저장)

for i in range(1, N):
    if time_table[i][0] < class_room[0]:    # 종료시간 전에 수업이 시작되는 경우
        heapq.heappush(class_room, time_table[i][1])    # 현재 시작되는 수업의 종료시간 추가(강의실 +1)
    else:
        heapq.heappop(class_room)    # 앞선 강의 종료
        heapq.heappush(class_room, time_table[i][1])    # 현재 시작되는 강의 종료시간 추가

print(len(class_room))    # 모든 강의 시작시간을 확인 후 현재 진행중인 강의 수 카운트