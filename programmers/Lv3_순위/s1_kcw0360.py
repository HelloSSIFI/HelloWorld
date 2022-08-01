def solution(n, results):
    answer = 0
    check = [[0] * n for _ in range(n)]    # 결과 체크

    for game in results:
        check[game[0]-1][game[1]-1] = 1    # 승
        check[game[1]-1][game[0]-1] = -1    # 패

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or check[i][j] != 0:    # 나 자신이 아니거나 승패가 확정된 경우는 skip
                    continue

                if check[i][k] == check[k][j] == 1:    # i가 k에게 이기고 k가  j에게 이긴 경우
                    check[i][j] = 1    # i도 j에게 이긴 것이 된다.
                    check[j][i] = check[k][i] = check[j][k] = -1    # 위의 경우를 제외한 나머지는 패처리
    print(check)
    for i in check:
        if i.count(0) == 1:    # 0이 1개인 경우는 자신을 제외한 모든 사람들과 승패 관계를 알 수 있기 때문에 이 경우만 확인한다.
            answer += 1

    return answer



print(solution(	5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))