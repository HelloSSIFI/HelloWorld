import sys
input = sys.stdin.readline


def find_set(x):                                # 원소 x의 대표원소를 찾아줌
    if leader[x] == x: return x                 # x가 대표원소일 경우 자신을 리턴
    leader[x] = find_set(leader[x])             # 아닐경우 x의 대표원소를 재귀를 이용하여 찾아주고
    return leader[x]                            # 대표원소를 리턴


def union(x, y):                                # 두 원소를 같은 집합으로 합쳐주는 함수
    leader[find_set(x)] = find_set(y)           # x의 대표원소가 바라보는 값을 y의 대표원소로 바꿔줌


answer = []
for tc in range(1, int(input()) + 1):
    n = int(input())
    k = int(input())
    leader = [i for i in range(n)]
    for i in range(k):                          # 친구 정보 k개를 각각 입력받아
        a, b = map(int, input().split())        # 두 원소를 같은 집합으로 합쳐줌
        union(a, b)

    answer.append(f'Scenario {tc}:')
    m = int(input())
    for i in range(m):                          # m개의 쌍을 입력받아
        u, v = map(int, input().split())        # 같은 집합에 속하면 1, 아니면 0을 출력
        if find_set(u) == find_set(v): answer.append('1')
        else: answer.append('0')
    answer.append('')

print('\n'.join(answer))
