def solution(n, costs):
    def find_set(x):                            # 원소의 대표값을 반환하는 함수
        if leader[x] == x:
            return x

        leader[x] = find_set(leader[x])
        return leader[x]


    def union_set(x, y):                        # 집합 x의 대표원소를 y의 대표원소로 바꿔주는 함수
        leader[find_set(x)] = find_set(y)


    leader = list(range(n))
    costs.sort(key=lambda x: x[2])              # 비용 기준 오름차순 정렬
    answer = cnt = 0
    for a, b, c in costs:
        if find_set(a) == find_set(b):          # 이미 연결된 섬이면 다음반복
            continue

        answer += c                             # 비용에 현재 두 섬을 연결하는 비용 추가
        cnt += 1                                # 다리개수 +1
        union_set(a, b)                         # 두 섬을 하나의 집합으로 바꿔줌
        if cnt == n - 1:                        # 모든 섬이 연결되면 반복종료
            break

    return answer


# print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
