N = int(input())

numbers = list(map(int, input().split()))

cnt = 0    # 소수 개수 카운팅
for i in numbers:
    result = []    # 약수 저장

    # 약수 찾기
    for j in range(1, i+1):
        if i % j == 0:
            result.append(j)

    # 약수가 두개면 소수 (1, input)라 판단 하여 카운팅 하기
    if len(result) == 2:
        cnt += 1

print(cnt)
