import sys
input = sys.stdin.readline


def in_frame(r, c, v):
    return True if 0 <= r < h and 0 <= c < n and 0 <= v < m else False


m, n, h = map(int, input().split())
frame = [[] for _ in range(h)]

total, ripe, un = 0, [], 0

for k in range(h):

    for i in range(n):
        line = list(map(int, input().split()))

        for j in range(m):

            # 토마토가 들어있다면
            if line[j] >= 0:
                total += 1

                # 익은 토마토
                if line[j] == 1:
                    # k층 i행 j열 위치
                    ripe.append([k, i, j])

                # 덜 익은 토마토
                else:
                    un += 1

        frame[k].append(line)

# 6방향
direct = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
answer = 0

# 안 익은 토마토 개수가 0이 될 때까지
while un != 0:
    answer += 1

    # 새로 추가될 익은 토마토
    new_ripe = []

    for now in ripe:
        # i층 j행, k열 위치의 익은 토마토
        i, j, k = now

        # 6방향 탐색
        for x, y, z in direct:
            ni, nj, nk = i+x, j+y, k+z

            # 격자 안일 때
            if in_frame(ni, nj, nk) and frame[ni][nj][nk] == 0:
                frame[ni][nj][nk] = 1
                new_ripe.append([ni, nj, nk])
                un -= 1


    # 새로 익은 토마토들로 목록 교체
    if new_ripe:
        ripe = new_ripe

    else:
        # 덜 익은 토마토가 남아 있는데 익힌 토마토가 없다면
        # 앞으로 토마토를 익힐 수 가 없으므로 -1
        print(-1)
        break

else:
    print(answer)