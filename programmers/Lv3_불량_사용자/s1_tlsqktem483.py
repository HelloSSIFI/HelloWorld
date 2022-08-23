from itertools import permutations


def solution(user_id, banned_id):
    answer = []
    n, m = len(user_id), len(banned_id)

    def check(id, compare):
        if len(id) != len(compare):
            return False

        else:
            for idx in range(len(id)):
                if id[idx] == '*':
                    continue
                elif id[idx] != compare[idx]:
                    return False
        return True

    for p in permutations(user_id, m):
        flag = True

        for i in range(m):
            if not check(banned_id[i], p[i]):
                flag = False

        if flag and set(p) not in answer:
            answer.append(set(p))

    return len(answer)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))