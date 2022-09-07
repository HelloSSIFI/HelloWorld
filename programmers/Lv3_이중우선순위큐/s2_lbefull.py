import heapq

def solution(operations):
    answer = [0, 0]
    min_heap = []                                               # 최소힙
    max_heap = []                                               # 최대힙
    cnt_dict = dict()                                           # 요소의 개수를 저장할 딕셔너리
    for op in operations:
        com, num = op.split()
        num = int(num)
        if com == 'I':                                          # 삽입연산일 경우
            heapq.heappush(min_heap, num)                       # 최소힙과 최대힙에 넣어주고
            heapq.heappush(max_heap, -num)                      # 해당 요소 카운트
            cnt_dict[num] = cnt_dict.get(num, 0) + 1
        elif cnt_dict:                                          # 힙에 요소가 있다면
            if num == 1:                                        # 최대값을 삭제시키는 연산이면
                while not cnt_dict.get(-max_heap[0]):           # 최대힙에서 해당 요소가 있을때까지 요소를 지워주고
                    heapq.heappop(max_heap)                     # 존재하는 요소이면 n으로 받아옴
                n = -heapq.heappop(max_heap)
            else:                                               # 최소값 삭제도 마찬가지
                while not cnt_dict.get(min_heap[0]):
                    heapq.heappop(min_heap)
                n = heapq.heappop(min_heap)
            cnt_dict[n] -= 1                                    # n으로 삭제시킨 값을
            if cnt_dict[n] == 0:                                # 딕셔너리에서 1줄여주고 해당요소가 0이라면
                cnt_dict.pop(n)                                 # 딕셔너리에서 삭제
    if cnt_dict:
        while not cnt_dict.get(-max_heap[0]):                   # 최대값과 최소값을 넣어줄 때도
            heapq.heappop(max_heap)                             # 해당 요소가 있을때까지 제거해준뒤
        while not cnt_dict.get(min_heap[0]):                    # answer에 추가
            heapq.heappop(min_heap)
        answer = [-max_heap[0], min_heap[0]]
    return answer
