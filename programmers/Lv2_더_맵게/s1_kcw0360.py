import heapq

def solution(scoville, K):
    answer = 0
    heap = scoville
    heapq.heapify(heap)  # 리스트를 힙으로 변환하기

    # 힙변환시 기본값이 최소힙이기 때문에 0번 idx가 최소값
    # K보다 스코빌 지수가 작을 때까지 반복
    while heap[0] < K:
        new = heapq.heappop(heap) + heapq.heappop(heap) * 2  # 새로운 지수의 매운맛 생성
        heapq.heappush(heap, new)  # heap에 넣기
        answer += 1
        # 스코빌지수가 한개가 남아 더이상 생성하지 못할 경우 -1 리턴
        if len(heap) == 1 and heap[0] < K:
            return -1
    return answer