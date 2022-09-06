def solution(queue1, queue2):
    answer = -1
    q = queue1 + queue2
    total = sum(q)
    target = total // 2                     # 두 큐의 합이 같다는 말 -> 큐 하나의 모든 요소의 합이 (전체 요소의 합 // 2) 
    p1 = 0                                  # queue1의 첫번째 요소를 가리키는 포인터
    p2 = len(queue1)                        # queue2의 첫번째 요소를 가리키는 포인터
    now = sum(queue1)                       # queue1 값 기준
    
    cnt = 0
    flag = False
    while p1 < p2 and p2 < len(q):
        if now == target:                   # 현재 queue1의 요소 합이 target 값과 같다면 
            flag = True                     # 다른 queue2의 요소 합도 queue1과 같을 것이므로 break
            break
            
        if now < target:                    # 현재 queue1의 요소 합이 target 값보다 작다면
            now += q[p2]                    # queue2에서 요소를 빼 queue1에 더해줌
            p2 += 1                         # queue2의 포인터 1 증가
        elif now > target:                  # 현재 queue1의 요소 합이 target 값보다 크다면
            now -= q[p1]                    # queue1의 맨 앞 요소를 빼줌(queue1의 요소 합이 target과 맞기만 하면되므로 queue2에 더해주는 작업은 필요 없음)
            p1 += 1                         # queue1의 포인터 1 증가  
        
        cnt += 1
    if flag:
        answer = cnt

    
    return answer