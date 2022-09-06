# 백준 12969번 ABC와 유사한 문제(재귀 DP)
# point) 각 경우에 따른 상태 트리(dp)를 구성해나가면서 주어진 조건에 맞는 경우가 생기면 값을 return

def search(table, i, a, b, c, prev = 0, pprev = 0, ans = ''):
    if i == len(S):
        if table['A'] == a and table['B'] == b and table['C'] == c:
            # 출근 횟수가 모두 일치하다면 곧바로 return
            return ans
        return None

    if dp[a][b][c][prev][pprev]:
        return

    dp[a][b][c][prev][pprev] = True

    # A 출근
    if a < table['A']:
        case1 = search(table, i + 1, a + 1, b, c, 1, prev, ans + 'A')  
        if case1:
            return case1

    # B 출근
    # 전날 B가 출근한 적이 없을 때만 B 출근 가능
    if b < table['B'] and prev != 2:
        case2 = search(table, i + 1, a, b + 1, c, 2, prev, ans + 'B')
        if case2:
            return case2
        
    # C 출근
    # 전날과 전전날 C가 출근한 적이 없을 때만 C 출근 가능
    if c < table['C'] and prev != 3 and pprev != 3:
        case3 = search(table, i + 1, a, b, c + 1, 3, prev, ans + 'C')
        if case3:
            return case3

    return None

S = input()
table = {
    'A' : 0, 'B': 0, 'C': 0
}
for c in S:
    table[c] += 1


# dp[a 출근 횟수][b 출근 횟수][c 출근 횟수][전날 출근자][전전날 출근자]
# 출근자 A : 1, B : 2, C : 3

'''
DP[3][3][3][4][4] 라고 가정(A와 B와 C의 출근횟수가 각각 3회인 경우)
일종의 상태 트리를 구성

0                                                                                                           |                      1                          |                        2                      |
0                                                            |         1           |          2             |       0              1                  2
0                                   |      1           2     | 0      1      2     |     ....    ....       |
0,         1,         2,        3   |   ... ....  |  ... ... |  ... ...  ... ...   |    ....  .... ....     |
0,1,2,3 | 0,1,2,3 | 0,1,2,3 |0,1,2,3|

*상태 의미 예시
DP[0][1][1] :  오늘까지 A는 출근하지 않고 B와 C만 1회 출근했다.
DP[1][1][0][1][0] : 오늘까지 A와 B가 1회 출근하였고 C는 출근하지 않았으며 전날 출근자는 A였다.
'''



dp = [[[[[0 for _ in range(4)] for _ in range(4)] for _ in range(len(S) + 1)] for _ in range(len(S) + 1)] for _ in range(len(S) + 1)]

result = search(table, 0, 0, 0, 0)
if result:
    print(result)
else:
    print(-1)

