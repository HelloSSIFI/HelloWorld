def solution(brown, yellow):
    total = brown + yellow

    for v in range(3, total//3+1):
        if total%v==0:
            r = total//v
            # 노랑의 개수 == 가로 - 2 * 세로 - 2
            # 브라운 개수 == (가로-1)*2 + (세로-1)*2
            if (v-2)*(r-2)==yellow and (v-1)*2+(r-1)*2==brown:
                return [r, v]