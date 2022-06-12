def solution(N, number):
    answer = 1
    dp = [set() for _ in range(9)]

    while answer < 9:
        temp = set()                                    # 현재 N을 사용한 개수에서 나올 수 있는 수의 범위를 저장
        for i in range(1, (answer + 1) // 2 + 1):       # 현재 개수의 반만큼 반복
            for num1 in dp[i]:                          # dp의 두 인덱스를 더했을 때 answer이 되는 집합끼리 연산
                for num2 in dp[answer - i]:
                    temp.add(num1 + num2)
                    temp.add(num1 - num2)
                    temp.add(num2 - num1)
                    temp.add(num1 * num2)
                    if num2:
                        temp.add(num1 // num2)
                    if num1:
                        temp.add(num2 // num1)

        dp[answer].update(temp)                         # 연산 후 answer 인덱스에 갱신
        dp[answer].add(int(str(N) * answer))            # N을 answer개 이어붙인 수도 추가

        if number in dp[answer]:                        # 원하는 수가 나왔다면
            break                                       # 반복 종료
        answer += 1                                     # 아니라면 answer+1 후 다시 반복

    else:                                               # 반복이 끝났는데 발견을 못했으면 -1
        answer = -1

    return answer

# print(solution(5, 12))                # 7 ^ (N - 1) 보다는 작을듯
