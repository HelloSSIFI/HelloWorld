import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)                 # 스코빌 지수를 힙으로 바꿔줌
    while scoville[0] < K:                  # 스코빌 지수의 제일 작은값이 K보다 작은동안 반복
        if len(scoville) < 2:               # 만약 음식이 2개 미만으로 남았다면
            answer = -1                     # 결과를 -1로 바꾸고 반복 종료
            break                           # 아니라면 결과+1 후 문제에 맞게 섞어서 스코빌 지수에 다시 넣어줌
        answer += 1
        heapq.heappush(scoville, heapq.heappop(scoville) + 2 * heapq.heappop(scoville))
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))
