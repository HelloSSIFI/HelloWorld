import sys
input = sys.stdin.readline

def find_set(x):                        # 대표원소를 찾는 함수
    if group[x] == x:                   # 대표원소일 경우 자신을 반환
        return x
    
    group[x] = find_set(group[x])       # 아닐 경우 자신의 대표원소를 재귀를 통해 바꿔주고
    return group[x]                     # 대표원소 반환


def union_set(x, y):                    # 두 집합을 합쳐주는 함수
    group[find_set(x)] = find_set(y)    # x의 대표원소를 y의 대표원소로 바꿔줌


V, E = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(E)]
lines.sort(key=lambda x: x[2])                                  # 가중치를 기준으로 오름차순 정렬
group = list(range(V + 1))

cnt = 0
i = 0
result = 0
while cnt < V - 1:                                              # V - 1 개의 선을 찾을때까지 반복
    if find_set(lines[i][0]) != find_set(lines[i][1]):          # 입력된 간선정보에서 두 정점의 대표원소가 다르면
        cnt += 1                                                # cnt + 1
        result += lines[i][2]                                   # 결과값에 가중치를 더해줌
        union_set(lines[i][0], lines[i][1])                     # 두 간선의 대표원소를 맞춰줌
    
    i += 1                                                      # 다음 간선 확인

print(result)
