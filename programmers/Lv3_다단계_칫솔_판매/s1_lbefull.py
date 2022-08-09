import sys
sys.setrecursionlimit(20000)


def solution(enroll, referral, seller, amount):
    answer = []


    def find_cost(name, par):                   # 모든 트리 순회
        for n in tree.get(name, []):            # 트리의 자식이 있다면
            find_cost(n, name)                  # 먼저 탐색
        
        for i in range(len(cost[name])):        # 현재 노드의 이익금 리스트를 순회
            charge = cost[name][i] // 10        # 10% 를 charge로 계산
            cost[name][i] -= charge             # 현재 이익금에서 10%를 빼주고
            if charge:                          # 0원 이상이라면
                cost[par].append(charge)        # 부모 노드에 추가


    tree = dict()
    cost = dict()
    for i in range(len(referral)):                              # tree에 자식 노드 정보를 저장
        tree[referral[i]] = tree.get(referral[i], [])           # cost에 각 이름들을 빈 리스트로 초기화
        tree[referral[i]].append(enroll[i])
        cost[enroll[i]] = []
    cost['-'] = []                                              # 민호의 이름 대신 - 이므로 -도 초기화
    for i in range(len(seller)):                                # 판매한 사람들을 순회하면서
        cost[seller[i]].append(amount[i] * 100)                 # 판매량 * 100을 해서 이익금 리스트에 추가
    
    find_cost('-', '-')                                         # 루트 노드부터 트리 탐색
    for name in enroll:                                         # enroll 순서대로 answer에 최종 이익금 추가
        answer.append(sum(cost[name]))
    return answer


# print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))
