T = int(input())
for tc in range(1, T+1):
    A = list(map(int, input().split()))
    print(sorted(A)[-3])