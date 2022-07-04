def search(r, c, room):
    for i in range(5):
        for j in range(5):
            if (r, c) != (i, j) and abs(r-i) + abs(c-j) <= 2 and room[i][j] == "P":
                # 가로
                if r == i:
                    if c > j and room[r][j+1] == "X":
                        continue
                    elif j > c and room[r][c+1] == "X":
                        continue
                    else:
                        return True
                # 세로
                elif c == j:
                    if r > i and room[i+1][c] == "X":
                        continue
                    elif i > r and room[r+1][c] == "X":
                        continue
                    else:
                        return True
                # 대각선
                else:
                    if room[r+(i-r)][c] == "X" and room[r][c+(j-c)] == "X":
                        continue
                    return True
    return False


def solution(places):
    ans = []

    for p in places:
        flag = False
        for r in range(5):
            if flag:
                continue
            for c in range(5):
                if flag:
                    continue
                if p[r][c] == "P":
                    flag = search(r, c, p)
        if flag:
            ans.append(0)
        else:
            ans.append(1)

    return ans

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))