from collections import defaultdict


def solution(n, build_frame):
    def chk_v(x, y, c):                                                                             # (x, y)위치에 현재 기둥상태가 가능한지 확인
        if v[x, y]:                                                                                 # 기둥이 있다면
            if y == 0 or v[x, y - 1] or h[x, y] or h[x - 1, y]:                                     # 조건대로 바닥인지, 다른 기둥 위인지, 보의 한쪽 끝인지 확인
                return True                                                                         # 조건이 맞다면 True
            return False                                                                            # 조건이 맞지 않다면 False

        if c: return True                                                                           # 함수의 깊이가 1 이상이면 True
        return chk_h(x, y + 1, c + 1) and chk_h(x - 1, y + 1, c + 1) and chk_v(x, y + 1, c + 1)     # 기둥이 없다면 위에 기둥 상태, 위의 양옆에 보가 가능한지 재귀하여 모두 가능할 경우 True


    def chk_h(x, y, c):                                                                             # (x, y) 위치에 현재 보 상태가 가능한지 확인
        if h[x, y]:                                                                                 # 기둥과 마찬가지로 확인
            if v[x, y - 1] or v[x + 1, y - 1] or (h[x - 1, y] and h[x + 1, y]):                     # 보가 있다면 조건과 맞추어 가능하면 True, 아니면 False
                return True                                                                         # 함수 깊이가 1 이상이면 True
            return False                                                                            # 보가 없을 때 주변 상황이 모두 True라면 True를 반환

        if c: return True
        return chk_v(x, y, c + 1) and chk_v(x + 1, y, c + 1) and chk_h(x - 1, y, c + 1) and chk_h(x + 1, y, c + 1)


    answer = []
    v, h = defaultdict(int), defaultdict(int)           # key에는 좌표를 넣고, value에는 각각 v는 기둥, h는 보가 있다면 1을 넣어줌
    vh, chk = [v, h], [chk_v, chk_h]
    for x, y, a, b in build_frame:
        vh[a][x, y] = b                                 # 작업 정보대로 기둥 또는 보를 설치 또는 삭제해줌
        if not chk[a](x, y, 0):                         # 해당 작업을 체크하여 가능한지 확인
            vh[a][x, y] ^= 1                            # 불가능하다면 원상복구

    for x in range(n + 1):
        for y in range(n + 1):
            if v[x, y]: answer.append([x, y, 0])
            if h[x, y]: answer.append([x, y, 1])

    return answer


# print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
