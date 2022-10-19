def solution(target):
    def dfs(s, cnt, snb, idx):                                      # s   : 현재까지 점수
        nonlocal answer                                             # cnt : 던진 횟수
        if cnt > answer[0]:                                         # snb : 싱글과 불을 합한 횟수
            return                                                  # idx : 이전 재귀함수의 마지막 인덱스

        if s == target:                                             # 던진횟수가 저장된 값을 넘어섰으면 리턴
            if cnt < answer[0]:                                     # 점수가 target과 같다면
                answer = [cnt, snb]                                 # 조건에 맞게 총 횟수와 싱글, 불 횟수를 저장

            elif snb > answer[1]:
                answer[1] = snb
            return

        if s + 60 * (answer[0] - cnt) < target:                     # 저장된 최소횟수에서 현재까지 던진횟수를 빼서 남은 횟수를 구하고
            return                                                  # 남은 횟수만큼 60점을 던져도 target 점수를 만들지 못하면 리턴

        for i in range(idx, len(score_list)):                       # 조합을 만들기 위해 반복
            if s + score_list[i] > target:                          # 점수가 초과한다면 다음반복
                continue
            if score_list[i] <= 20 or score_list[i] == 50:          # 싱글 또는 불이라면 cnt와 snb를 1 추가해서 재귀
                dfs(s + score_list[i], cnt + 1, snb + 1, i)         # 아니라면 cnt만 1 추가해서 재귀
            else:
                dfs(s + score_list[i], cnt + 1, snb, i)


    temp = 0
    while target > 600:                                             # 너무 큰 수는 최소값을 맞추기위해 최고 점수인 60으로 진행됨
        target -= 300                                               # 불 점수인 50과 60의 다트 개수 차이는 300점 일 때 1 차이이므로
        temp += 5                                                   # 점수 조합을 고려하여 1 ~ 600 까지의 점수는 dfs를 실행하고 그 이상의 점수는 300점 단위로 깎아서 60 * 5를 사용
    answer = [200000, 0]                                            # 정답 배열 초기화
    score_set = set([50])
    for i in range(1, 21):
        for j in range(1, 4):
            score_set.add(i * j)                                    # 다트 점수로 나올 수 있는 값을 모두 구해서 내림차순 정렬
    score_list = sorted(score_set, reverse=True)
    dfs(0, 0, 0, 0)
    answer[0] += temp                                               # 정답을 구한 뒤 빼주었던 점수들을 1개 60점으로 환산한 개수를 더해줌
    return answer


# print(solution(100000))
