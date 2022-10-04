r, c, k = map(int, input().split())
r, c = r - 1, c - 1
arr = [list(map(int, input().split())) for _ in range(3)]
answer = -1
for t in range(101):
    if 0 <= r < len(arr) and 0 <= c < len(arr[r]) and arr[r][c] == k:                   # 문제 조건을 달성했다면
        answer = t                                                                      # 시간을 기록하고 반복종료
        break
    
    flag = False
    if len(arr) < len(arr[0]):                                                          # 열이 길다면
        arr = list(map(list, zip(*arr)))                                                # 행과 열을 바꿔주고
        flag = True                                                                     # flag에 표시를 남겨줌

    max_len = 0
    for i in range(len(arr)):
        cnt = dict()
        for j in range(len(arr[i])):
            if arr[i][j]:                                                               # 행을 탐색하면서 숫자와 나온 회수를 기록
                cnt[arr[i][j]] = cnt.get(arr[i][j], 0) + 1

        cnt = sorted(cnt.items(), key=lambda x: (x[1], x[0]))                           # 회수 기준, 회수가 같다면 값 기준 오름차순 정렬
        arr[i] = [cnt[x][y] for x in range(len(cnt)) for y in range(len(cnt[x]))]       # 현재 행을 정렬한 값으로 다시 재생성
        max_len = max(max_len, len(arr[i]))                                             # 최대 열의 길이를 갱신
    
    for i in range(len(arr)):                                                           # 모든 행을 탐색
        while len(arr[i]) < max_len:                                                    # 열의 길이가 최대 열의 길이보다 짧다면
            arr[i].append(0)                                                            # 최대 열의 길이와 맞게 0을 채워줌
    
    if flag:                                                                            # 앞서 행과 열을 바꿨었다면
        arr = list(map(list, zip(*arr)))                                                # 다시 복구

print(answer)
