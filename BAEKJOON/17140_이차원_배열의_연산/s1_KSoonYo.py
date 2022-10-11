import sys
from collections import Counter
from itertools import chain

input = sys.stdin.readline

def fill(arr, max_length):
    for r in arr:
        if len(r) < max_length:
            r += ([0] * (max_length - len(r)))

# 행 연산
def row_calc(arr):
    
    max_length = 0
    remove_set = {0, }

    for i, row in enumerate(arr):  
        row = [j for j in row if j not in remove_set]                           # 0 원소 제거
        new_row = sorted(Counter(row).items(), key=lambda x : (x[1], x[0]))
        new_row = list(chain(*new_row))                                         # flatten
        max_length = max(max_length, len(new_row))
        arr[i] = new_row[:100]                                                  # 100개 이내 원소만 추출
    
    max_length = min(100, max_length)
    
    fill(arr, max_length)
    return max_length

# 열 연산
def col_calc(arr):
    # 연산 편의상 행렬 뒤집기
    new_arr = list(map(list, zip(*arr)))
    
    max_length = 0
    remove_set = {0, }
    
    for i, col in enumerate(new_arr):
        col = [j for j in col if j not in remove_set]
        new_col = sorted(Counter(col).items(), key=lambda x : (x[1], x[0]))
        new_col = list(chain(*new_col))
        max_length = max(max_length, len(new_col))
        new_arr[i] = new_col[:100]
    
    max_length = min(100, max_length)

    fill(new_arr, max_length)

    # 원상복귀
    arr = list(map(list, zip(*new_arr)))
    return arr, max_length

r, c, k = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(3)]
row_length, col_length = (3, 3)

t = 0
while t <= 100:

    if row_length >= r and col_length >= c and array[r - 1][c - 1] == k:
        print(t)
        exit()

    if row_length >= col_length:
        col_length = row_calc(array)
        
    else:
        array, row_length = col_calc(array)

    t += 1
    
print(-1)