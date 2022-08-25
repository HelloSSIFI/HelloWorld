def solution(user_id, banned_id):
    n, m = len(user_id), len(banned_id)

    visit = [0]*n
    ids = [[] for _ in range(m)]

    # i번째 user_id 를 banned_id 확인하며
    # j번째 banned_id체크에 통과하면 j번 banned_id 후보에 i를 넣음
    for i in range(m):
        for j in range(n):
            if len(user_id[j]) != len(banned_id[i]):continue

            l = len(user_id[j])
            for k in range(l):
                if banned_id[i][k] == '*' or user_id[j][k] == banned_id[i][k]:continue
                break

            else:
                ids[i].append(j)
                visit[j] = 1

    answer = set()

    # 가능한 조합을 찾는 dfs
    def dfs(cnt, s, now):
        nonlocal answer
        # m개의 banned_id를 모두 찾았다면 set에 now를 추가
        if cnt == m:
            answer.add(now)
            return
        # x번째 banned_id가 될 수 있는 후보를 돌면서 아직 추가가 안된 후보는 추가
        for x in range(s, m):
            for y in ids[x]:
                if visit[y]:
                    visit[y] = 0
                    dfs(cnt+1, x+1, now<<y)
                    visit[y] = 1
    dfs(0, 0, 1)
    return len(answer)

'''
def solution(user_id, banned_id):
    answer = []
    candidates = [[]]
    for b_id in banned_id:
        new_candidates = []
        for u_id in user_id:
            if len(u_id) != len(b_id):
                continue
            check = True
            for i in range(len(u_id)):
                if b_id[i] != '*' and u_id[i] != b_id[i]:
                    check = False
                    break
            if check:
                for c in candidates:
                    if u_id not in c:
                        new_candidates.append(c+[u_id])
        candidates = new_candidates
    for c in candidates:
        if set(c) not in answer:
            answer.append(set(c))

    return len(answer)
'''

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))