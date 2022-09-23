def solution(n, m, x, y, queries):
    col_start, row_start, col_end, row_end = y, x, y, x
    for d, dx in reversed(queries):
        if d == 0:
            if col_start != 0:
                col_start += dx
            col_end = min(m-1, col_end+dx)

        elif d == 1:
            col_start = max(0, col_start-dx)
            if col_end != m-1:
                col_end -= dx

        elif d == 2:
            if row_start != 0:
                row_start += dx
            row_end = min(n-1, row_end+dx)

        else:
            row_start = max(0, row_start-dx)
            if row_end != n-1:
                row_end -= dx

        if row_start > n-1 or row_end < 0 or col_start > m-1 or col_end < 0:
            return 0

    return (row_end-row_start+1)*(col_end-col_start+1)