N, K = map(int, input().split())        # N구, K개
arr = list(map(int, input().split()))   # 사용순서 배열
'''
멀티 탭에 전기용품을 꽂을 때 분류 3가지
1. 빈 구멍이 있을 때
    꽂고 pass
2. 이미 꽂혀 있을 때
    그냥 pass
3. 빈 구멍이 없을 때
    1) 이후 사용 예정이 없는 전기 용품
        swap
    2) 이후 사용 예정이 있는 전기 용품
        재사용 예정 전자 기기가 가장 먼 것을 뽑음
'''

tab = [0]*N                         # 실제 콘센트로 생각
ans = swap = num = max_l = 0
'''
ans: 결과값, swap: 뽑을 콘센트 위치, num: arr를 탐색하는 인덱스, max_l: 재사용 예정인 전자 기기의 사용 번호
'''
for item in arr:
    if item in tab:                 # 이미 꼽혀있는 경우
        pass

    elif 0 in tab:                  # 빈 구멍이 있는 경우
        tab[tab.index(0)] = item

    else:                           # 빈 구멍이 없는 경우
        for el in tab:
            if el not in arr[num:]:             # 이후 재사용 없는 전자 기기 swap
                swap = el
                break
            elif arr[num:].index(el) > max_l:   # 재사용 예정 & 가장 늦게 재사용 하는 것 찾기
                max_l = arr[num:].index(el)     # 인덱스 담음
                swap = el                       # 해당 전자 기기 번호

        tab[tab.index(swap)] = item             # swap!
        max_l = swap = 0                        # reset
        ans += 1

    num += 1

print(ans)