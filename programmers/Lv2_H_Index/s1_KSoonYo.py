def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort()                    # 정렬
    for i in range(n):
        if citations[i] >= (n - i):     # 전체 길이에서 현재 인덱스 번호를 뺀 값 : h 기준(현재 인덱스보다 오른쪽에 있는 값들은 현재 값보다 모두 큼)
            answer =  n - i
            break                                                       
    
    return answer