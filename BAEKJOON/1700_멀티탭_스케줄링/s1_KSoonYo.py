import sys
input = sys.stdin.readline

N, K = map(int, input().split())
schedule = list(map(int, input().split()))
plugs = []

cnt = 0
for app_idx in range(K):
    # 이미 있는 가전 기구라면 pass
    if schedule[app_idx] in plugs:
        continue

    # 플러그에 자리가 남았다면 플러그 인
    if len(plugs) < N:
        plugs.append(schedule[app_idx])
        continue

    unplugged_idx = 0
    far_distance = 0
    for plug in plugs:
        # 플러그에 있는 가전 기구 중 나중에 쓰지 않는 기구 플러그 아웃  
        if plug not in schedule[app_idx:]:
            unplugged_idx = plugs.index(plug)
            break
        # 현재 플러그에 있는 기구 중 가장 나중에 사용될 기구를 플러그 아웃
        # 가장 나중에 사용되는지 여부를 알기 위한 거리 체크
        distance = schedule[app_idx:].index(plug)
        if far_distance < distance:
            far_distance = distance
            unplugged_idx = plugs.index(plug)


    plugs[unplugged_idx] = schedule[app_idx]
    cnt += 1

print(cnt)

'''
27% fail
잘못된 그리디 전략: 전체 사용 순서에서 현재 플러그에 있는 기구 중 '가장' 마지막에 사용되는 기구를 뽑음

전체 사용 순서에서 가장 마지막에 있는 기구의 플러그를 뽑는 것이 아니라
현재 플러그에 있는 기구 중 다음에 사용될 순서가 가장 나중인 것을 뽑아야 한다.

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
plugs = [0] * N
plug_idx = 0

used_table = list(map(int, input().split()))
electronics = [0] * (K + 1)

for idx in range(K):
    electronics[used_table[idx]] += 1

cnt = 0

for used_idx in range(K):
    used_electronic = used_table[used_idx]
    if not plugs[plug_idx]:
        # 플러그에 자리가 남았다면 꽂아준다.
        plugs[plug_idx] = used_electronic
        electronics[used_electronic] -= 1
        plug_idx = (plug_idx + 1) % N
        continue

    elif used_electronic in plugs:
        # 사용하려는 가전기구가 플러그에 이미 꽂아 있다면 건너 뛰기
        electronics[used_electronic] -= 1
        continue

    # 플러그에 자리가 없고 뽑아야 하는 상황일 때
    unplugged = False
    for idx in range(N):
        if not electronics[plugs[idx]]:
            # 이후에 한 번도 사용하지 않는 플러그는 빼버린다.
            unplugged_idx = idx
            unplugged = True
            break        
    
    # 뽑힌 플러그가 없다면 
    # 현재 사용 중인 가전 기구 중 가장 나중에 쓰는 가전 기구를 우선 뽑아서 다른 가전 기구로 교체
    if not unplugged:
        for latest_idx in range(K - 1, used_idx, -1):
            if used_table[latest_idx] in plugs:
                unplugged_idx = plugs.index(used_table[latest_idx])
                break
        
    # 플러그에 있는 것들 중 이후에 사용하지 않는 것이거나 가장 나중에 사용하는 것을 뽑는다.
    plugs[unplugged_idx] = used_electronic
    if electronics[used_electronic]:
        electronics[used_electronic] -= 1
    cnt += 1

print(cnt)
'''

