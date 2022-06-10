n, k = map(int, input().split())
multitap = list(map(int, input().split()))

plugs = []
ans = 0

for i in range(k):
    if multitap[i] in plugs:
        continue
    if len(plugs) < n:
        plugs.append(multitap[i])
        continue

    # 빈도수가 없는 플러그 제거를 위한 index 변수
    temp = 0
    idx = 0

    for plug in plugs:
        # 재사용 없는 플러그는 제거
        if plug not in multitap[i:]:
            idx = plug
            break

        # 빈도수가 가장 적은 인덱스 제거
        elif multitap[i:].index(plug) > temp:
            temp = multitap[i:].index(plug)
            idx = plug

    # 인덱스 제거 & 새로운 인덱스 추가 & ans 중첩
    plugs[plugs.index(idx)] = multitap[i]
    ans += 1

print(ans)