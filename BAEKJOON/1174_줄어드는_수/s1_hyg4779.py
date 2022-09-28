from collections import deque

n = int(input())

if n > 1023:
    print(-1)
    exit()
else:
    results = list(range(10))
    queue = deque([(str(num), num) for num in range(1, 10)])

    while queue:
        number, now = queue.popleft()

        for i in range(now):
            new = number+str(i)
            queue.append((new, i))
            results.append(new)

    print(results[n-1])