import heapq
n = int(input())
lectures = []

for _ in range(n):
    a, b = map(int, input().split())
    heapq.heappush(lectures, (b, a))

answer, using = 0, [lectures[0][0]]

for i in range(1, n):
    end, start = lectures[i]

    tmp = heapq.heappop(using)

    if tmp > start:
        heapq.heappush(using, tmp)

    heapq.heappush(using, end)
    answer = max(answer, len(using))

print(answer)