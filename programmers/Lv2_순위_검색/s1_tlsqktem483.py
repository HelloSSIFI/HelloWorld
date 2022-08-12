"""
아이디어 : query 마다 info 를 다 탐색
효율성 Fail
"""
def solution(info, query):
    answer = []
    for q in query:
        q = q.replace('and ', '')
        q = q.split()
        cnt = 0

        for i in info:
            i = i.split()
            flag = True

            if int(i[-1]) < int(q[-1]):
                flag = False
            else:
                for j in range(len(q)-1):
                    if q[j] == '-':
                        continue
                    elif q[j] != i[j]:
                        flag = False
                        break

            if flag:
                cnt += 1
        answer.append(cnt)
    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))