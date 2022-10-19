N, K = map(int, input().split())
A = list(map(int, input().split()))
cnt = dict()
num = 0
for i in range(N):                      # 주어진 배열의 0 ~ i를 더한 값을 key, 개수를 value로 하여
    num += A[i]                         # cnt에 저장
    cnt[num] = cnt.get(num, 0) + 1

prev = 0
answer = 0
for i in range(N):                      # i번 이전까지의 합을 prev에 받아옴
    answer += cnt.get(prev + K, 0)      # 합이 K가 되어야 하므로 prev + K 값을 찾아서 개수를 더해줌
    prev += A[i]                        # 다음 반복을 위해 prev에 현재 숫자를 더해주고
    cnt[prev] -= 1                      # cnt에서 개수를 1 빼줌

print(answer)
