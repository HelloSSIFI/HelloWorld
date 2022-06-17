import sys
# 참고: https://velog.io/@ready2start/Python-%EB%B0%B1%EC%A4%80-2293-%EB%8F%99%EC%A0%84-1
# DP 문제 핵심
# 1) 전체의 문제를 부분 문제로 나누기
# 2) 부분 문제의 결과값을 메모이제이션
# 3) 부분 문제의 결과값들 간 관계식을 점화식으로 구성
# DP 공부 팁: https://stonejjun.tistory.com/48

 
input = sys.stdin.readline

n, k = map(int, input().split())

coins = []

for _ in range(n):
    coins.append(int(input()))

count_list = [0] * (k + 1)
# x원짜리 동전 하나로 x원을 만드는 경우의 수 = 1
count_list[0] = 1

for i in coins:
    for j in range(i, k + 1):
        count_list[j] += count_list[j - i]

print(count_list[k])