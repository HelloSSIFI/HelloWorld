import heapq

n = int(input())

lectures = [list(map(int, input().split())) for _ in range(n)]
lectures.sort()

# room = [lectures[0][1]]
room = []
heapq.heappush(room, lectures[0][1])

for i in range(1, n):
    if room[0] <= lectures[i][0]:
        heapq.heappop(room)
    heapq.heappush(room, lectures[i][1])

print(len(room))