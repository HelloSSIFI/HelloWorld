import sys
input = sys.stdin.readline


def check():                                # 막대를 던저 파괴된 미네랄에 인접한 좌표에
    i = 0                                   # 떨어지는 클러스터가 있는지 확인하는 함수
    while i < len(Q):                       # 있다면 True, 없다면 False를 반환
        r, c = Q[i]

        if r == R - 1:                      # Q를 이용한 BFS 방식으로 탐색하여
            return False                    # Q에 맨 아래줄 좌표가 담긴다면 False, 아니라면 True

        for d in range(4):                  # Q에서 요소를 뺄 때 제거가 아닌 인덱스를 옮겨가면서 빼오므로
            nr = r + dr[d]                  # True 일 때, Q에는 떠있는 미네랄의 모든 좌표가 담기게 됨
            nc = c + dc[d]
            if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] == 'x' and not visited[nr][nc]:
                Q.append([nr, nc])
                visited[nr][nc] = 1

        i += 1
    return True


def gravity():                                          # 떠있는 클러스터를 땅 혹은 미네랄을 만날때까지 내려주는 함수
    bottom = []                                         # 클러스터의 각 열에 맨 아래좌표를 담아줄 리스트
    for r, c in Q:
        if arr[r + 1][c] == '.':
            bottom.append([r, c])
    
    flag = False
    while True:
        for r, c in bottom:                             # 반복문의 탈출 조건
            if r == R - 1 or arr[r + 1][c] == 'x':      # 현재 r이 맨 아래(땅)있거나, 자신의 아래에 미네랄이 있다면
                flag = True                             # while 반복문 종료
                break
        
        if flag:
            break
        
        for r, c in Q:                                  # 현재 Q에 있는 모든 좌표(떠있는 클러스터)를
            arr[r][c] = '.'                             # 빈 공간으로 변경

        for i in range(len(Q)):                         # Q의 모든 요소의 r좌표를 1씩 늘려줌
            Q[i][0] += 1
        
        for i in range(len(bottom)):                    # bottom도 마찬가지
            bottom[i][0] += 1
        
        for r, c in Q:                                  # Q의 모든 좌표를 미네랄로 변경
            arr[r][c] = 'x'


R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]
N = int(input())
stick = list(map(lambda x: R - int(x), input().split()))                    # 막대의 높이를 현재 arr에 맞게 재조정
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for i in range(N):
    d = 1                                                                   # 막대를 던지는 부분
    c = 0                                                                   # 인덱스를 2로 나눈 나머지를 이용하여
    if i % 2:                                                               # 순서에 맞게 번갈아가며 왼쪽에서 던질지 오른쪽에서 던질지 결정
        d = -1
        c = C - 1
    
    r = stick[i]
    flag = False
    Q = []
    visited = [[0] * C for _ in range(R)]
    while 0 <= c < C:
        if arr[r][c] == 'x':                                                # 막대를 던저 처음 미네랄을 만나면
            arr[r][c] = '.'                                                 # 미네랄을 파괴
            for nr, nc in [[r - 1, c], [r + 1, c], [r, c + d]]:             # 파괴된 미네랄의 3방향(막대가 날아온 방향은 볼 필요가 없음) 탐색
                if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] == 'x':      # 해당 방향에 미네랄이 있다면
                    Q = []                                                  # Q에 넣어주고 방문처리 후
                    visited = [[0] * C for _ in range(R)]                   # check 함수를 이용하여 떠있는 클러스터가 있는지 확인
                    Q.append([nr, nc])                                      # 문제 조건에 의해 두 개 이상의 클러스터가 동시에 떨어지는 경우는 없으므로
                    visited[nr][nc] = 1                                     # check 함수를 통과한 방향이 있다면 바로 break
                    if check():
                        flag = True
                        break
            break
        c += d
    
    if Q and flag:                                                          # Q가 있고 check 함수를 통과했다면
        gravity()                                                           # 중력 작용

*map(lambda x: print(''.join(x)), arr),
