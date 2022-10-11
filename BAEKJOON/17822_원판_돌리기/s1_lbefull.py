import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def rotate(x, d, k):                        # 번호가 x인 원판을 d방향으로 k칸 회전시키는 함수
    sign = -1                               # 직접 회전시키지는 않고 시작 인덱스를 옮기는 방식으로 조정
    if d:                                   # 방향에 따라 시작 인덱스에 더해줄지 빼줄지 결정하여
        sign = 1                            # k만큼 이동 후 M으로 나눈 나머지를 저장
    start[x] += k * sign
    start[x] %= M


def rm(i, j, cnt):                          # 인접하면서 같은 수를 찾아 제거하는 함수
    global flag                             # 만약 하나라도 있다면 flag를 조정
    if not circle[i][j]:                    # 현재 수가 0이라면 종료
        return

    eq = []                                 # 인접하면서 같은 수의 좌표를 담을 리스트
    a = j - start[i]                        # 인접한 4방향을 확인하면서 수가 같으면 담아줌
    for ni, nj in [[i, j + 1], [i, j - 1], [i + 1, start[i + 1] + a], [i - 1, start[i - 1] + a]]:
        nj %= M
        if circle[i][j] == circle[ni][nj]:
            eq.append((ni, nj))

    if cnt or eq:                           # 현재 함수가 맨 처음 호출된 것이 아니라면 현재 수를 그냥 지워주고
        flag = False                        # 맨 처음 호출된 함수라면 eq에 요소가 있을 경우에만 현재 수를 지워줌
        circle[i][j] = 0

    for ni, nj in eq:                       # eq에 있는 좌표들로 재귀
        rm(ni, nj, cnt + 1)


def flat():                                 # 평균에 1씩 가깝게 만들어주는 함수
    avg = 0
    cnt = 0
    for i in range(1, N + 1):
        for j in range(M):
            if not circle[i][j]:            # 0이 아닌 수들의 평균을 구해줌
                continue
            avg += circle[i][j]
            cnt += 1
    if cnt:                                 # 모두 0일 경우도 이 함수가 실행되므로
        avg /= cnt                          # cnt가 0 이상일 때 나누어줌

    for i in range(1, N + 1):
        for j in range(M):
            if not circle[i][j]:            # 원판의 모든 수를 확인
                continue

            if circle[i][j] < avg:          # 평균보다 작으면 1 키워주고 크면 1 줄여줌
                circle[i][j] += 1

            elif circle[i][j] > avg:
                circle[i][j] -= 1


N, M, T = map(int, input().split())
circle = [[0] * M] + [list(map(int, input().split())) for _ in range(N)] + [[0] * M]
rotation = [list(map(int, input().split())) for _ in range(T)]
start = [0] * (N + 2)

for x, d, k in rotation:                    # T번 회전
    for i in range(x, N + 1, x):            # x의 배수들을 회전
        rotate(i, d, k)

    flag = True                             # 인접한 같은 수가 있는지 확인할 변수
    for i in range(1, N + 1):               # 모든 원판의 수를 확인하여
        for j in range(M):                  # rm함수로 인접한 같은 수를 제거
            rm(i, j, 0)

    if flag:                                # 인접한 수가 없다면
        flat()                              # 평균으로 1씩 가까워지도록 평탄화 함수 호출

answer = 0
for i in range(1, N + 1):
    answer += sum(circle[i])
print(answer)
