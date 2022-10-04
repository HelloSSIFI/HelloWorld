import sys
import heapq

input = sys.stdin.readline

N = int(input())
courses = []
for _ in range(N):
    S, T = map(int, input().split())
    courses.append((S, T))



courses.sort(key=lambda x : x[0])           # 강의 시작 시간 순으로 정렬(최대한 한 강의실에서 이전 강의 시간과 다음 강의 시간 사이 공백을 줄이기 위함)
rooms = []                                  # 일찍 끝나는 강의 순으로 최소힙 유지

for course in courses:
    s, t = course
    if rooms and rooms[0][0] <= s:          # 가장 빨리 끝나는 강의 종료 시간보다 강의 시작 시간이 늦다면
        heapq.heappop(rooms)                # 해당 강의실을 이용 가능

    heapq.heappush(rooms, (t, s))           # 끝나는 시간이 빠른 순으로 정렬

print(len(rooms))
