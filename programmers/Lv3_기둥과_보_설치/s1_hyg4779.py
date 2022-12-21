def impossible(result):
    bo, col = 1, 0

    for x, y, a in result:
        # 기둥일 때
        if a == col:
            if y != 0 and (x, y-1, col) not in result and \
                    (x-1, y, bo) not in result and (x, y, bo) not in result:
                return True

        # 보일 때
        else:
            if (x, y-1, col) not in result and (x+1, y-1, col) not in result and \
                    not ((x-1, y, bo) in result and (x+1, y, bo) in result):
                return True

    return False

def solution(n, build_frame):
    built = set()

    for x, y, a, b in build_frame:
        # 현재 아이템 위치와 종류
        item = (x, y, a)

        # 추가일 때
        if b:
            built.add(item)
            if impossible(built):
                built.remove(item)

        # 삭제할 때
        elif item in built:
            built.remove(item)
            if impossible(built):
                built.add(item)
    answer = map(list, built)

    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))


solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]])