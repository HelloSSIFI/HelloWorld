import sys
input = sys.stdin.readline


N, M = map(int, input().split())
S = set()
for _ in range(N):                      # 집합 S에 해당하는 문자열들을
    S.add(input().strip())              # 셋에 넣어줌

answer = 0
for _ in range(M):                      # 주어진 M개의 문자열을 순회
    if input().strip() in S:            # S에 포함되는 문자열이면
        answer += 1                     # answer+1

print(answer)
