def find_set(x):                                # 네트워크의 대표원소를 찾아주는 함수
    if leader[x] == x:                          # 자신이 대표원소이면 자신을 반환
        return x
    leader[x] = find_set(leader[x])             # 아니라면 leader의 값을 대표원소로 바꿔주고
    return leader[x]                            # 대표원소를 반환


def union_set(x, y):                            # 두 컴퓨터를 하나의 네트워크로 합쳐주는 함수
    leader[find_set(x)] = leader[find_set(y)]   # 한 컴퓨터의 대표를 다른 컴퓨터의 대표로 바꿔줌


def solution(n, computers):
    global leader
    leader = list(range(n))                     # 처음에는 자신만의 네트워크로 설정
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j]:                 # 두 컴퓨터간에 네트워크가 되어있다면
                union_set(i, j)                 # 하나로 합쳐줌
    for i in range(n):
        find_set(i)                             # 대표원소를 갱신해주고
    leader = set(leader)                        # 중복을 제거하여 개수를 반환
    return len(leader)


# print(solution(3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
