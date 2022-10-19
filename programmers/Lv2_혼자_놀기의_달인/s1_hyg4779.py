from collections import deque
def solution(cards):
    '''
    만들 수 있는 모든 그래프를 그리고,
    그래프의 길이를 graphes에 담아서
    모든 곱의 조합을 찾아서 최대값 리턴
    '''
    answer = 0
    cards = [0]+cards

    n = len(cards)
    graphes = []
    visit = [0]*(n+1)

    for i in range(1,n):
        if visit[i] == 0:

            Q = deque([cards[i]])
            cnt = 0
            while Q:
                now = Q.popleft()
                cnt += 1

                visit[now] = 1
                next = cards[now]
                if visit[next] == 0:
                    Q.append(next)

            graphes.append(cnt)

    for i in range(len(graphes)-1):
        for j in range(i+1, len(graphes)):
            answer = max(answer, graphes[i]*graphes[j])

    return answer


print(solution([8, 6, 3, 7, 2, 5, 1, 4]))