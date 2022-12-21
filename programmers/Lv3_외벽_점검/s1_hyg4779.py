from itertools import permutations
import math


def solution(n, weak, dist):
    m = len(weak)
    # 전부다 시계방향으로 돈다고 가정하여
    # 두번째 점이 첫번 째 점으로 가기위해 첫번째 점 위치 + 원형 크기를 더해서 추가해줌
    weak = weak + [w + n for w in weak]

    minCnt = math.inf
    # 시작지점
    for start in range(m):
        # 보낼 친구들 순열
        for d in permutations(dist, len(dist)):
            # 보낸 친구 수, # 현재 위치
            cnt, pos = 1, start

            for i in range(1, m):
                # 다음 위치
                nextPos = start + i
                # 다음 위치까지 차이
                diff = weak[nextPos] - weak[pos]

                # 다음 거리가 갈 수 있는 거리보다 멀다면
                # 친구+1, 다음 위치로 시작
                if diff > d[cnt-1]:
                    pos = nextPos
                    cnt += 1
                    # 모든 친구를 보냈다면 break
                    if cnt > len(dist):
                        break

            # 순열을 돌고, 보낸 친구수 최솟값 갱신
            if cnt <= len(dist):
                minCnt = min(minCnt, cnt)

    if minCnt == math.inf:
        return -1

    return minCnt

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))