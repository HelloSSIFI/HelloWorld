import sys
input = sys.stdin.readline


N, M = map(int, input().split())

n_s = []
for _ in range(N):
    n_s.append(input())

m_s = []
for _ in range(M):
    m_s.append(input())

answer = 0
for m in m_s:    # M개의 문자열을 차례대로 N개의 문자열에 포함되는지 확인
    if m in n_s:
        answer += 1

print(answer)