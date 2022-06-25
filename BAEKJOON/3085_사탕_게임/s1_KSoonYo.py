import sys
input = sys.stdin.readline

N = int(input())
candy_map = [list(input().strip()) for _ in range(N)]
crush = [[], []]
cnt = 0

def crush_check():
    global cnt

    idx = 0
    while idx < N:                                              # 전체 행, 열 탐색 & 길이 count
        crush[0] = candy_map[idx]
        crush[1] = list(map(lambda x : x[idx], candy_map))
        crush_row, crush_col = crush
        r_candy = crush_row[0]
        c_candy = crush_col[0]
        r_cnt = 0
        c_cnt = 0
        r_temp = 0
        c_temp = 0
        for k in range(N):
            if r_candy == crush_row[k]:
                r_temp += 1

            else:
                r_cnt = max(r_cnt, r_temp)
                r_candy = crush_row[k]
                r_temp = 1
            
            if c_candy == crush_col[k]:
                c_temp += 1
            
            else:
                c_cnt = max(c_cnt, c_temp)
                c_candy = crush_col[k]
                c_temp = 1

            if k == N - 1:
                r_cnt = max(r_cnt, r_temp)   
                c_cnt = max(c_cnt, c_temp)

        cnt = max(cnt, max(r_cnt, c_cnt))
        idx += 1


for i in range(N):
    for j in range(N - 1):
        if candy_map[i][j] != candy_map[i][j + 1]:                                                  # 색깔이 다른 곳
            candy_map[i][j], candy_map[i][j + 1] = candy_map[i][j + 1], candy_map[i][j]             # 좌 우 교환
            crush_check() 
            candy_map[i][j + 1], candy_map[i][j] = candy_map[i][j], candy_map[i][j + 1]             # 원상복구

        if i < N - 1 and candy_map[i][j] != candy_map[i + 1][j]:                                    # 상 하 교환
            candy_map[i][j], candy_map[i + 1][j] = candy_map[i + 1][j], candy_map[i][j]
            crush_check()
            candy_map[i + 1][j], candy_map[i][j] = candy_map[i][j], candy_map[i + 1][j]             # 원상복구


print(cnt)

