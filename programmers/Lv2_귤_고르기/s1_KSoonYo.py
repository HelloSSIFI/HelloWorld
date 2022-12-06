from collections import Counter, deque

# key point: 가장 개수가 많은 귤부터 판다.
def solution(k, tangerine):
    answer = 0
    tangerine = list(Counter(tangerine).items())            # 귤의 종류별 개수 count
    tangerine.sort(key=lambda x : -x[1])                    # 내림차순 정렬
    q = deque(tangerine)                                    # deque화
    while q:
        typ, cnt = q.popleft()
        answer += 1
        
        if cnt >= k:                             # 귤의 개수가 k보다 같거나 많으면 answer return
            return answer
        
        if cnt < k:                              # 귤의 개수가 k보다 작으면 k에서 귤의 개수를 뺀다.
            k -= cnt
            
    return answer