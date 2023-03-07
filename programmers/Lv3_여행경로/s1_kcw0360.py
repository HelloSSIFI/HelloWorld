from collections import Counter
import copy


def solution(airline_tickets):
    answer = []
    tickets = []
    for f, t in airline_tickets:
        tickets.append((f, t))
    tickets_cnt = Counter(tickets)    # 중복 티켓 카운트

    def dfs(visited, check):
        if len(visited) == len(tickets) + 1:    # 모든 곳을 다 방문했을 경우 answer에 경로 추가
            answer.append(copy.deepcopy(visited))
            return

        for ticket in tickets:
            if ticket[0] == visited[-1] and check[ticket] > 0:    # 현 위치가 출발지인 티켓이 존재하는 경우
                visited.append(ticket[1])    # 방문 체크
                check[ticket] -= 1    # 티켓 소모
                dfs(visited, check)    # 다음 장소로 이동
                check[ticket] += 1
                visited.pop()

    dfs(['ICN'], tickets_cnt)
    answer.sort()    # 알파벳 순서대로 정렬

    return answer[0]    # 알파벳 순서가 가장 빠른 경로를 return