from collections import defaultdict, deque

tree = defaultdict(list)
answer = 0
was = []

def find_sheep(q, sheep, wolf):
    global answer

    if answer < sheep:
        answer = sheep

    for i in range(len(q)):
        t = q.popleft()
        if was[t] == 1:    # 해당 구역에 늑대가 있을 떄
            if sheep > wolf+1:    # 해당 구역의 늑대 수를 합한 값이 양의 수 보다 적어야 양 모으기 가능
                q.extend(tree[t])
                find_sheep(q, sheep, wolf+1)
                for _ in range(len(tree[t])):
                    q.pop()
        else:    # 양일 경우 +1 한 후 다음 으로 이동
            q.extend(tree[t])
            find_sheep(q, sheep+1, wolf)
            for _ in range(len(tree[t])):
                q.pop()
        q.append(t)

def solution(info, edges):
    global was
    was = info

    # 그래프
    for a, b in edges:
        tree[a] += [b]

    q = deque()
    q.append(0)    # 0부터 시작

    find_sheep(q, 0, 0)

    return answer

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))