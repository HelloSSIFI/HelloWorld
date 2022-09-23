def solution(k, dungeons):
    answer = -1
    sequences = []

    # 모든 조합 생성
    def perm(now):
        if len(now) == len(dungeons):
            sequences.append(now)
        for i in range(len(dungeons)):
            if i in now:continue
            perm(now+[i])


    for j in range(len(dungeons)):
        perm([j])


    # 만들어진 조합 모두 돌아보기
    for queue in sequences:
        sta = k
        cnt = 0
        for x in queue:
            need, use = dungeons[x]
            if sta < need:break
            sta -= use
            cnt += 1
        answer = max(answer, cnt)

    return answer

print(solution(80, [[80, 20], [50, 40], [30, 10]]))