import sys
import copy
input = sys.stdin.readline

def left(boards):
    # 가장 왼쪽 열을 기준으로 swap
    for blocks in boards:
        p1, p2 = 0, 1
        while p2 < N:
            if p1 != p2:
                if blocks[p1] and blocks[p1] == blocks[p2]:
                    blocks[p1] += blocks[p2]
                    blocks[p2] = 0
                    p1 += 1
                
                elif not blocks[p1] and blocks[p2]:
                    blocks[p1], blocks[p2] = blocks[p2], blocks[p1]
                elif blocks[p1] and blocks[p2]:
                    p1 += 1
                    continue
                p2 += 1
            else:
                p2 += 1        
    return boards


def right(boards):
    # 가장 오른쪽 열을 기준으로 swap
    for blocks in boards:
        p1, p2 = N - 1, N - 2
        while p2 >= 0:
            if p1 != p2:
                if blocks[p1] and blocks[p1] == blocks[p2]:
                    blocks[p1] += blocks[p2]
                    blocks[p2] = 0
                    p1 -= 1
                    
                elif not blocks[p1] and blocks[p2]:
                    blocks[p1], blocks[p2] = blocks[p2], blocks[p1]
                elif blocks[p1] and blocks[p2]:
                    p1 -= 1
                    continue
                p2 -= 1
            else:
                p2 -= 1 
    return boards

def up(boards):    
    # 가장 위쪽 행을 기준으로 swap
    for i in range(len(boards)):
        p1, p2 = 0, 1
        while p2 < N:
            if p1 != p2:
                if boards[p1][i] and boards[p1][i] == boards[p2][i]:
                    boards[p1][i] *= 2
                    boards[p2][i] = 0
                    p1 += 1
                elif not boards[p1][i] and boards[p2][i]:
                    boards[p1][i], boards[p2][i] = boards[p2][i], boards[p1][i]
                elif boards[p1][i] and boards[p2][i]:
                    p1 += 1
                    continue
                p2 += 1
            else:
                p2 += 1   
    return boards

def down(boards):
    # 가장 아래쪽 행을 기준으로 swap
    for i in range(len(boards)):
        p1, p2 = len(boards) - 1, len(boards) - 2
        while p2 >= 0:
            if p1 != p2:
                if boards[p1][i] and boards[p1][i] == boards[p2][i]:
                    boards[p1][i] *= 2
                    boards[p2][i] = 0
                    p1 -= 1
                elif not boards[p1][i] and boards[p2][i]:
                    boards[p1][i], boards[p2][i] = boards[p2][i], boards[p1][i]
                elif boards[p1][i] and boards[p2][i]:
                    p1 -= 1
                    continue
                p2 -= 1
            else:
                p2 -= 1
    return boards



def dfs(boards, cnt):
    global maxV
    if cnt == 5:
        for blocks in boards:
            maxV = max(maxV, max(blocks))
        return
    dfs(up(copy.deepcopy(boards)), cnt + 1)
    dfs(down(copy.deepcopy(boards)), cnt + 1)
    dfs(left(copy.deepcopy(boards)), cnt + 1)
    dfs(right(copy.deepcopy(boards)), cnt + 1)

N = int(input())
boards = [list(map(int, input().split())) for _ in range(N)]
maxV = 0
dfs(copy.deepcopy(boards), 0)
print(maxV)

