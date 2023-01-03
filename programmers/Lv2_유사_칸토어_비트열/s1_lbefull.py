def solution(n, l, r):
    def cantor(n, dep, x, cnt, target):
        if x == target:                                                         # l 또는 r까지 구간이 되었다면
            return cnt                                                          # 구간까지 1의 개수(cnt) 리턴

        nx = x + 5 ** n                                                         # 현재 n단계 비트열이므로 비트열의 5구간중 한 구간을 더한 구간을 nx로 구해줌
        if nx > target:                                                         # nx가 찾는 구간을 넘어서면 n단계를 1단계 줄임
            if dep == 3:                                                        # dep는 11011 이 반복되는 총 5개의 영역 중 몇번 째 영역인지 표현
                return cnt                                                      # 3번째 영역은 1이 없으므로 재귀할 필요없이 현재까지 1의 개수 cnt를 리턴
            return cantor(n - 1, 1, x, cnt, target)                             # 3번째 영역이 아니면 n에서 1단계를 줄이고 1영역부터 탐색하여 target에 맞춤

        if dep != 3:                                                            # nx가 구간보다 작다면
            cnt += 4 ** n                                                       # 3영역이 아닐경우 1의 개수를 더해줌(1의 개수는 11011이 반복되므로 4의 n제곱)
        return cantor(n, dep + 1, nx, cnt, target)                              # dep를 1올려서 재귀


    answer = cantor(n - 1, 1, 0, 0, r) - cantor(n - 1, 1, 0, 0, l - 1)          # 1 ~ r까지 구간에서 1 ~ (l - 1) 구간까지 1의 개수를 빼줌
    return answer


# print(solution(2, 4, 17))
