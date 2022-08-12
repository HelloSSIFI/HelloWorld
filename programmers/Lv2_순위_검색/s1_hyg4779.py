def solution(info, query):

    n, m = len(info), len(query)
    answer = [0]*m

    for i in range(n):
        lang, job, career, food, score = info[i].split()
        tmp = f'{lang[0]}{job[0]}{career[0]}{food[0]}'
        for j in range(m):
            sql = query[j].split()

            # tmp를 도는 변수, sql을 도는 변수
            k, l = 0, 0
            while k < 4:
                if sql[l] == '-' or tmp[k] == sql[l][0]:
                    k += 1
                    l += 2
                else:break

            else:
                if int(sql[l-1]) - int(score) <= 0:
                    answer[j] += 1




    return answer


print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))
