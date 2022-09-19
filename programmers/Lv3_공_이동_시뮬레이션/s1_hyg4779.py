def solution(n, m, x, y, queries):

    si, sj, ei, ej = x, y, x, y

    for idx, power in queries[::-1]:
        # 열 감소
        if idx == 0:
            if sj == 0:
                ej = min(m-1, ej+power)
            else:
                if sj+power >= m:return 0

                sj = min(m-1, sj+power)
                ej = min(m-1, ej+power)

        # 열 증가
        elif idx == 1:
            if ej == m-1:
                sj = max(0, sj-power)
            else:
                if ej-power < 0: return 0

                sj = max(0, sj-power)
                ej = max(0, ej-power)

        # 행 감소
        elif idx == 2:
            if si == 0:
                ei = min(n-1, ei+power)
            else:
                if si+power >= n: return 0

                si = min(n-1, si+power)
                ei = min(n-1, ei+power)

        # 행 증가
        else:
            if ei == n-1:
                si = max(0, si-power)
            else:
                if ei+power < 0: return 0

                si = max(0, si-power)
                ei = max(0, ei-power)

    return (ei-si+1)*(ej-sj+1)

print(solution(2, 2, 0, 0, [[2, 1], [0, 1], [1, 1], [0, 1], [2, 1]]))
print(solution(2, 5, 0, 1, [[3, 1], [2, 2], [1, 1], [2, 3], [0, 1], [2, 1]]))