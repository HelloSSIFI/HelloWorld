import sys
input = sys.stdin.readline

n = int(input())
total = 0

arr = [[0]*(n+1)]
for _ in range(n):
    line = [0]+list(map(int, input().split()))
    arr.append(line)
    total += sum(line)

answer = float('inf')


for i in range(1, n+1):
    for j in range(1, n+1):
        for d1 in range(1, n+1):
            for d2 in range(1, n+1):
                if i+d1+d2 > n or j-d1 < 1 or j+d2 > n:
                    continue

                mat = [[0]*(n+1) for _ in range(n+1)]
                people = [0]*5

                mat[i][j] = 5
                for k in range(1, d1+1):
                    mat[i+k][j-k] = 5

                for k in range(1, d2+1):
                    mat[i+k][j+k] = 5

                for k in range(1, d2+1):
                    mat[i+d1+k][j-d1+k] = 5

                for k in range(1, d1+1):
                    mat[i+d2+k][j+d2-k] = 5


                # 1선거구
                for r in range(1, i+d1):
                    for c in range(1, j+1):
                        if mat[r][c] == 5:
                            break
                        people[0] += arr[r][c]

                # 2선거구
                for r in range(1, i+d2+1):
                    for c in range(n, j, -1):
                        if mat[r][c] == 5:
                            break
                        people[1] += arr[r][c]

                # 3선거구
                for r in range(i+d1, n+1):
                    for c in range(1, j-d1+d2):
                        if mat[r][c] == 5:
                            break
                        people[2] += arr[r][c]

                # 4선거구
                for r in range(i+d2+1, n+1):
                    for c in range(n, j-d1+d2-1, -1):
                        if mat[r][c] == 5:
                            break
                        people[3] += arr[r][c]

                people[4] = total - sum(people[:4])
                answer = min(answer, max(people)-min(people))

print(answer)