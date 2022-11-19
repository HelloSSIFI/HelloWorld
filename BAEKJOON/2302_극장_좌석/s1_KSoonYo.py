
# pypy3 통과
import sys

input = sys.stdin.readline

# i와 i+1번째가 자리를 뒤바꾼 상태, 바꾸지 않은 상태별로 seats를 배치해서 다음 좌석 번호로 넘긴다.
def search(N, seats, vips, i = 1):
    global cnt

    # 현재 번호가 마지막 좌석 번호라면
    if i >= N:
        cnt += 1
        return

    # 현재 자리와 다음 자리를 바꾸지 않는다면
    search(N, seats, vips, i + 1)

    # 현재 자리와 다음 자리를 바꾼다면
    # 단, 현재 자리와 다음 자리는 vip석이 아니어야 함
    if i + 1 <= N and i not in vips and (i + 1) not in vips:
        seats[i], seats[i + 1] = seats[i + 1], seats[i]
        search(N, seats, vips, i + 2)
        seats[i], seats[i + 1] = seats[i + 1], seats[i]                 # 변경한 자리에 대해 원상복구

    return




N = int(input())
vips = set()
for _ in range(int(input())):
    vips.add(int(input()))

seats = [i for i in range(N + 1)]
cnt = 0
search(N, seats, vips)
print(cnt)


# 경우의 수와 곱의 법칙을 활용한 solution (DP)
# https://mygumi.tistory.com/132
