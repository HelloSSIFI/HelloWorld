from copy import deepcopy as dc
import sys
input = sys.stdin.readline

# els에 값과 색 집어넣기
# el[0]: 값, el[1]: 색
n = int(input())
els = []
for _ in range(n):
    tmp = [list(input().split()) for _ in range(8)]
    vals, cols = list(), list()
    for line in range(4):
        vals.append(tmp[line])
        cols.append(tmp[line+4])
    els.append((vals, cols))


# 조합 만들기
sequence = []
def perm(now):
    if len(now)==3:
        sequence.append(now)
        return

    for j in range(n):
        if j not in now:
            perm(now+[j])


for num in range(n):
    perm([num])


colors = [['']*5 for _ in range(5)]
field = [[0]*5 for _ in range(5)]
answer = 0


# value: 숫자값, bomb: 색, turn: 재료 순서
def dfs(value, bomb, turn):
    global answer

    # 3번째 재료 까지 끝났으면 계산
    if turn == 3:
        result = {'R': 0, 'B': 0, 'G': 0, 'Y': 0, 'W': 0}
        for r in range(5):
            for c in range(5):
                result[bomb[r][c]] += value[r][c]
        res = 7*result['R'] + 5*result['B'] + 3*result['G'] + 2*result['Y']
        answer = max(answer, res)
        return

    # 폭탄 값이 음수면 0, 9초과면 9
    def adj_val(tmp):
        if tmp < 0:
            tmp = 0
        elif tmp > 9:
            tmp = 9
        return tmp

    # 값 계산

    for i in range(2):
        for j in range(2):
            n_value, n_bomb = dc(value), dc(bomb)
            for k in range(4):
                for l in range(4):
                    x, y = n_value[i+k][j+l], n_bomb[i+k][j+l]

                    n_value[i+k][j+l] = adj_val(x+int(val[turn][k][l]))
                    n_bomb[i+k][j+l] = bomb[i+k][j+l] if bom[turn][k][l]=='W' else bom[turn][k][l]

            dfs(n_value, n_bomb, turn+1)




for seq in sequence:
    # 재료들
    val = [els[seq[0]][0], els[seq[1]][0], els[seq[2]][0]]
    bom = [els[seq[0]][1], els[seq[1]][1], els[seq[2]][1]]

    # 각 재료들 4번씩 회전
    for a in range(4):
        for b in range(4):
            for c in range(4):
                # 채워넣을 격자
                field = [[0]*5 for _ in range(5)]
                colors = [['W']*5 for _ in range(5)]

                dfs(field, colors, 0)
                val[0] = list(zip(*val[0][::-1]))
                bom[0] = list(zip(*bom[0][::-1]))

            val[1] = list(zip(*val[1][::-1]))
            bom[1] = list(zip(*bom[1][::-1]))

        val[2] = list(zip(*val[2][::-1]))
        bom[2] = list(zip(*bom[2][::-1]))

print(answer)