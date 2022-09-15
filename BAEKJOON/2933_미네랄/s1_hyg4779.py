R, C = map(int, input().split())
# 동굴
arr = [list(input().split()) for _ in range(R)]
# 던진 막대들 높이
stick = [int(input()) for _ in range(int(input()))]

def move():
    for i in range(R-1):
        for j in range(C):
            if arr[i][j]=='x' and arr[i+1][j]=='.':
                arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]