N, K = map(int, input().split())
prod = list(map(int, input().split()))
using = dict()                          # key: 제품 번호, value: 다음 사용 여부
result = 0

for i in range(K):                      # 전기 용품 순회
    if prod[i] in using:                # 이미 꽂혀있는 제품이면
        continue                        # 다음 반복

    if len(using) < N:                  # 멀티탭에 추가할 공간이 있다면
        using[prod[i]] = 0              # 추가 후 다음 반복
        continue

    result += 1                         # 위 두 경우가 아니라면 멀티탭에서 하나를 빼야하므로 결과 +1

    for k in using:                     # 우선 꽂혀있는 제품들의 value를 0으로 만들어줌
        using[k] = 0

    for j in range(i, K):                                   # 현재 제품 다음으로 쓰는 제품부터 순회
        if (prod[j] in using) and using[prod[j]] == 0:      # 만약 현재 꽂혀있는 것이고 이전에 한번도 안나왔으면
            using[prod[j]] = j                              # value를 j로 바꿔줌

    if min(using.values()) == 0:                            # 만약 꽂혀있는 제품중 이후에 한번도 안쓰는 제품이 있으면
        using.pop(min(using, key=using.get))                # 해당 제품을 빼주고
    else:                                                   # 모든 제품이 다시 사용된다면
        using.pop(max(using, key=using.get))                # 제일 늦게 사용되는 제품을 빼줌

    using[prod[i]] = 0                                      # 현재 제품을 사용중에 추가

print(result)
