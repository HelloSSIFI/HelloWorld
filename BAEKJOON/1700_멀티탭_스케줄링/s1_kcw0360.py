N, K = map(int, input().split())

appliances = list(map(int, input().split()))
multitap = []
unplug = 0

for i in range(K):
    # 멀티탭에 중복으로 사용하는 것이 없을 경우 추가
    if len(multitap) <= N and appliances[i] not in multitap:
        multitap.append(appliances[i])
    # 멀티탭에 꽂을 수 있는 것이 초과했을 때
    if len(multitap) > N:
        temp = -1
        for j in range(N):
            app = appliances[i + 1:K]    # 추후 사용해야할 용품들
            if multitap[j] not in app:    # 추후 재사용 물건이 없을 경우
                multitap.remove(multitap[j])
                unplug += 1
                break
            else:
                maxi = max(temp, app.index(multitap[j]))    # 추후 재사용 예정이 있는 경우 가장 마지막에 사용할 물건 찾기
        if len(multitap) > N:
            multitap.remove(app[temp])    # 가장 마지막에 쓸 물건 제거
            unplug += 1

print(unplug)