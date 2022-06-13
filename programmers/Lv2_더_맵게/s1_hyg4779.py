import heapq

def solution(scoville, K):
    ans = 0
    l = len(scoville)

    heapq.heapify(scoville)                 # 최초 힙정렬

    while len(scoville) > 1:                # 2개 이상 일때만 실행
        tmp = heapq.heappop(scoville)

        if tmp >= K:                        # 제일 작은 요소가 K 이상이면 break
            break

        else:                               # 계산과정
            two = heapq.heappop(scoville)
            tmp += two*2
            heapq.heappush(scoville, tmp)
            ans += 1

    if scoville[0] >= K:                    # 1개만 남았을 경우 K 이상인지 검사
        return ans

    return -1


# print(solution([1,2,3],  11))