import sys, math
input = sys.stdin.readline


N = int(input())
lines = [[] for _ in range(N + 1)]
for _ in range(N - 1):                                                  # 트리 정보 저장
    a, b = map(int, input().split())
    lines[a].append(b)
    lines[b].append(a)

D = G = 0                                                               # ㄷ모양 트리의 개수를 D, ㅈ모양 트리의 개수를 G에 저장
for i in range(1, N + 1):                                               # ㄷ모양 트리의 개수는 ㄷ모양에서 가운데 2개의 정점에서
    if len(lines[i]) > 1:                                               # 각각 끝방향으로 가는 선의 개수를 구해서 곱해준 것과 같음
        for j in lines[i]:                                              # 모든 정점을 탐색하면서 위 방식대로 구할 경우 방향만 다른 경우가 중복되므로
            if len(lines[j]) > 1:                                       # 모든 개수를 구한 뒤 2로 나누어줌
                D += (len(lines[i]) - 1) * (len(lines[j]) - 1)          # ㅈ모양 트리의 개수는 한 정점만 3개의 간선을 가지므로 모든 정점을 탐색하면서
    G += math.comb(len(lines[i]), 3)                                    # 간선들 중 3개를 조합으로 뽑는 개수를 더해줌

D //= 2
answer = 'D'
if 3 * G > D: answer = 'G'
elif 3 * G == D: answer = 'DUDUDUNGA'
print(answer)
