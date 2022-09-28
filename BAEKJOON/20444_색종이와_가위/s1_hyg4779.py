n, k = map(int, input().split())

'''
row: 가위질을 가로로 자른 횟수
col: 가위질을 세로로 자른 횟수
n = row + col
조각의 개수는 (row+1)*(col+1)
따라서 row가 정해지면 조각의 개수를 알 수 있음
+
조각의 개수는 row와 col의 횟수에 따르기 때문에 n까지가 아닌 n//2까지만 확인하면 됨
row와 col의 차이가 작아질수록 조각의 개수가 늘어남
'''

l, r = 0, n//2

while l <= r:
    row = (l+r)//2
    col = n-row

    pieces = (row+1)*(col+1)
    if k==pieces:
        print('YES')
        exit()

    if k > pieces:
        l = row+1
    else:
        r = row-1
else:
    print('NO')