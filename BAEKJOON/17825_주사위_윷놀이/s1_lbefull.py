def dfs(cnt, sc):
    global answer
    if cnt == 10:
        answer = max(answer, sc)                                                # 주사위를 10번 굴렸다면 점수 최대값을 저장
        return

    for i in range(4):                                                          # 4개의 말들을 각각 주사위 숫자만큼 움직여서 재귀
        l = dice[cnt] - 1
        prev = unit[i]
        if prev == 21:                                                          # 도착한 말이라면 다음반복
            continue

        nxt = load[prev][-1]                                                    # 처음 움직일 때는 경로가 2개라면 2번째를 선택
        while l > 0:                                                            # 나머지 칸은 1번째 경로로 이동
            if load[nxt]:
                nxt = load[nxt][0]
            l -= 1

        if nxt != 21 and (nxt in unit):                                         # 도착칸이 아니지만 다른 말이 해당칸에 있다면
            continue                                                            # 다음 반복

        unit[i] = nxt                                                           # 현재 말의 위치를 바꿔주고
        dfs(cnt + 1, sc + score[nxt])                                           # 재귀 후 다시 말의 위치를 복구
        unit[i] = prev


dice = list(map(int, input().split()))
load = [[] for _ in range(33)]                                                  # load에는 다음칸으로 갈 수 있는 번호를 모두 저장
score = [0] * 33                                                                # score는 현재 칸으로 오면 얻을 수 있는 점수를 저장
for i in range(32):
    score[i] = i * 2
    if i in {21, 24, 26}:
        continue
    load[i].append(i + 1)

for a, b in [[5, 22], [10, 25], [15, 27], [24, 30], [26, 30], [32, 20]]:        # load의 0번 인덱스는 계속 지나갈 때 사용할 번호이고
    load[a].append(b)                                                           # 1번 인덱스는 해당 자리에 있다면 처음 출발할 때만 사용

info = [13, 16, 19, 22, 24, 28, 27, 26, 25, 30, 35]
score[21] = 0
for i in range(22, 33):
    score[i] = info[i - 22]

unit = [0] * 4                                                                  # unit에는 말들의 위치를 저장
answer = 0
dfs(0, 0)
print(answer)
