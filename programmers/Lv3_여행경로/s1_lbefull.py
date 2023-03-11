def solution(tickets):
    tick_dict = {}
    for s, e in tickets:                                                    # tick_dict의 key에는 공항이름
        if s not in tick_dict:                                              # value에는 해당 공항에서 이동할 수 있는 공항들을
            tick_dict[s] = []                                               # 리스트 형태로 저장

        if e not in tick_dict:
            tick_dict[e] = []

        tick_dict[s].append(e)

    for k in tick_dict:                                                     # tick_dict의 각 value들을 내림차순 정렬
        tick_dict[k].sort(reverse=True)

    stack = ['ICN']                                                         # stack에는 시작 공항인 ICN을 넣어주고 반복문 실행
    answer = []
    while stack:                                                            # stack이 빌 때까지 반복
        top = stack[-1]                                                     # stack의 가장 위에 있는 요소를 top으로 받아옴
        if tick_dict[top]:                                                  # top에서 다음 공항으로 갈 수 있는 리스트가 있다면
            stack.append(tick_dict[top].pop())                              # stack에 그 중 하나를 추가(내림차순 정렬이므로 마지막 요소가 사전 순 제일 빠름)
        else:                                                               # 더 이상 갈 곳이 없다면
            answer.append(stack.pop())                                      # answer에 top을 추가하고 stack에서 top을 pop

    return answer[::-1]                                                     # answer에는 경로가 거꾸로 쌓이므로 뒤집에서 리턴


# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
