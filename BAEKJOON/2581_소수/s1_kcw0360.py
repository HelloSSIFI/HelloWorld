M = int(input())
N = int(input())


result = []    # 찾은 소수 값 저장
for i in range(M, N+1):
    temp = []    # 약수 임시 저장

    # 약수 찾기
    for j in range(1, i+1):
        if i % j == 0:
            temp.append(j)

    # 약수가 두개면 소수 (1, input)라 판단 하여 result에 추가
    if len(temp) == 2:
        result.append(i)

# result에 값이 없을시 -1 출력, 존재한다면 합과 최소값 출력
if result:
    print(sum(result))
    print(result[0])
else:
    print(-1)
