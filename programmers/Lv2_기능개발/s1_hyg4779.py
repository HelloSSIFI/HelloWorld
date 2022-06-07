def solution(progresses, speeds):
    answer = []

    day = 0             # 지나간 날짜
    tmp = 0             # 같이 완료한 작업의 수

    for idx in range(len(progresses)):
        pro = progresses[idx]       # 해당 작업의 진행률
        s = speeds[idx]             # 해당 작업의 속도

        pro += day*s                # 현재 작업의 진행률

        if pro >= 100:              # 100퍼가 넘어갔다면 완료 수 +1 continue
            tmp += 1
            continue

        elif pro < 100 and tmp:     # 100퍼가 안됐고, 완료한 작업들이 있다면 append
            answer.append(tmp)
            tmp = 0

        # (100-pro)//s: 현재 속도가 완료 될 기간
        if (100-pro)%s:             # 남은 날짜가 있다면 + 1
            day += (100-pro)//s + 1
        else:
            day += (100-pro)//s

        tmp += 1                    # 작업을 완료했으니 tmp + 1

    else:                           # 모든 작업 순회가 끝났는데 완료한 작업이 아직 append 안됐다면 실행
        if tmp:
            answer.append(tmp)

    return answer