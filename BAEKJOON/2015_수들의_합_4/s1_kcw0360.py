from collections import defaultdict
import sys
input = sys.stdin.readline


N, K = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
for i in range(1, len(arr)):
    arr[i] += arr[i-1]    # arr을 해당 0번 idx부터 i까지의 누적 합의 배열로 만든다.

check = defaultdict(int)
for num in arr:
    if num == K:    # 누적 합의 값이 K인 경우 answer +1
        answer += 1

    answer += check[num-K]    # K = arr[j] - arr[i]를 활용
    check[num] += 1    # 누적 합이 num이 되는 경우 추가

print(answer)