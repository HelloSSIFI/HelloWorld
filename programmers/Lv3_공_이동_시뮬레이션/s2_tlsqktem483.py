def solution(n, m, x, y, queries):
    # 목표지점으로 범위를 초기화
    sr, sc, er, ec = x, y, x, y

    # 역순으로 쿼리를 탐색
    for d, dx in reversed(queries):
        # 좌
        if d == 0:
            # 시작 col이 0인 경우,
            if sc == 0:
                # 끝 col의 범위를 갱신한다
                ec = min(m - 1, ec + dx)

            # 시작 col이 0이 아닌 경우,
            else:
                # 시작 col을 우측으로 dx만큼 이동한 결과가 m보다 크거나 같으면, 목표지점으로 갈 수 없기 때문에 return 0
                if sc + dx >= m: return 0

                # 시작 col과 끝 col의 범위를 갱신한다
                sc = min(m - 1, sc + dx)
                ec = min(m - 1, ec + dx)
        # 우
        elif d == 1:
            # 끝 col이 m-1인 경우,
            if ec == m - 1:
                # 시작 col의 범위를 갱신한다
                sc = max(0, sc - dx)

            # 끝 col이 m-1이 아닌 경우,
            else:
                # 끝 col을 좌측으로 dx만큼 이동한 결과가 0보다 작으면, 목표지점으로 갈 수 없기 때문에 return 0
                if ec - dx < 0: return 0

                # 시작 col과 끝 col의 범위를 갱신한다
                sc = max(0, sc - dx)
                ec = max(0, ec - dx)
        # 상
        elif d == 2:
            # 시작 row가 0인 경우,
            if sr == 0:
                # 끝 row의 범위를 갱신한다
                er = min(n - 1, er + dx)

            # 시작 row가 0이 아닌 경우,
            else:
                # 시작 row를 밑으로 dx만큼 이동한 결과가 n보다 크거나 같으면, 목표지점으로 갈 수 없기 때문에 return 0
                if sr + dx >= n: return 0

                # 시작 row와 끝 row의 범위를 갱신한다
                sr = min(n - 1, sr + dx)
                er = min(n - 1, er + dx)
        # 하
        else:
            # 끝 row가 n-1인 경우,
            if er == n - 1:
                # 시작 row의 범위를 갱신한다
                sr = max(0, sr - dx)

            # 끝 row가 n-1가 아닌 경우,
            else:
                # 끝 row를 위로 dx만큼 이동한 결과가 0보다 작으면, 목표지점으로 갈 수 없기 때문에 return 0
                if er + dx < 0: return 0

                # 시작 row와 끝 row의 범위를 갱신한다
                sr = max(0, sr - dx)
                er = max(0, er - dx)

    # 출발점이 될 영역의 칸 수 return
    return (er - sr + 1) * (ec - sc + 1)


# 시간복잡도 = O(n), 공간복잡도 = O(n)

print(solution(2, 2, 0, 0, 	[[2,1],[0,1],[1,1],[0,1],[2,1]]))
print(solution(2, 5, 0, 1, [[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]))
print(solution(1000, 1000, 1, 1, [[0,100001],[2,100001]]))