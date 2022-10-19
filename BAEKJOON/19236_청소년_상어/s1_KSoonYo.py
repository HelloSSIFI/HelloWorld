import sys
import copy
input = sys.stdin.readline


def routing(MAP, fish_table, s, sd, total):
    global maxV

    dirs = [0, [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
    copied_map = [arr[:] for arr in MAP]

    # 물고기 이동
    # 작은 물고기부터 이동, 빈 칸과 다른 물고기가 있는 칸은 이동 가능
    # 상어가 있거나 공간을 넘으면 x, 이동할 수 있는 칸을 향할 때까지 45도 반시계 방향 회전
    for fish in sorted(fish_table.keys()):
        
        if not fish_table[fish]:
            # 이미 잡아 먹힌 물고기라면 pass
            continue
        
        hr, hc, d = fish_table[fish]
        
        nr, nc = hr + dirs[d][0], hc + dirs[d][1]
        # 이동 가능 하다면
        if 0 <= nr < 4 and 0 <= nc < 4 and (nr, nc) != s:
            next_fish = copied_map[nr][nc]
            copied_map[hr][hc], copied_map[nr][nc] = copied_map[nr][nc], copied_map[hr][hc]
            
            # 다음 칸에 물고기가 있다면
            if next_fish:
                fish_table[fish] = [nr, nc, d]
                fish_table[next_fish] = [hr, hc, fish_table[next_fish][2]]
            else:
                fish_table[fish] = [nr, nc, d]

            continue

        # 이동이 불가능 하다면 -> 방향 회전
        for _ in range(7):
            d = (d + 1) % 9
            if not d:
                d = 1

            nr, nc = hr + dirs[d][0], hc + dirs[d][1]
            # 이동 가능 하다면
            if 0 <= nr < 4 and 0 <= nc < 4 and (nr, nc) != s:
                next_fish = copied_map[nr][nc]
                copied_map[hr][hc], copied_map[nr][nc] = copied_map[nr][nc], copied_map[hr][hc]
                if next_fish:
       

                    fish_table[fish] = [nr, nc, d]
                    fish_table[next_fish] = [hr, hc, fish_table[next_fish][2]]
                else:
                    fish_table[fish] = [nr, nc, d]
                break
    
 
    # 상어 진행 방향에 물고기가 있는지 체크, 없으면 return
    candidates = []
    sr, sc = s[0] + dirs[sd][0], s[1] + dirs[sd][1]
    while 0 <= sr < 4 and 0 <= sc < 4:
        if copied_map[sr][sc]:
            candidates.append((sr, sc))
        sr, sc = sr + dirs[sd][0], sc + dirs[sd][1]


    if not candidates:
        maxV = max(maxV, total)
        return

    # candidates 후보군을 돌면서 최대값 갱신
    # 해당 위치의 물고기를 잡아먹었다고 가정
    for cr, cc in candidates:
        catched = copied_map[cr][cc]
        sd = fish_table[catched][2]
        copied_map[cr][cc] = 0
        fish_table[catched] = []
        routing(copied_map, copy.deepcopy(fish_table), (cr, cc), sd, total + catched)
        copied_map[cr][cc] = catched
        fish_table[catched] = [cr, cc, sd]

MAP = [[0] * 4 for _ in range(4)]
fish_table = {}                                                             # 물고기 위치 저장

sd = 0
init = 0
for r in range(4):
    info = list(map(int, input().split()))
    for c in range(0, len(info), 2):
        if r == 0 and c // 2 == 0:
            init = info[c]
            sd = info[c + 1]
            fish_table[info[c]] = []
            MAP[r][c // 2] = 0
            continue
        MAP[r][c // 2] = info[c]                                            # 물고기 번호
        fish_table[info[c]] = [r, c // 2, info[c + 1]]                      # 물고기 번호: (r, c, 방향)


maxV = 0
routing(MAP, fish_table, (0, 0), sd, init)
print(maxV)
