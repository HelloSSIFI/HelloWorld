def solution(topping):
    answer = 0

    # 형, 동생이 가지고 있는 토핑과 그 개수
    old, young = dict(), dict()

    for i in topping:
        young[i] = young.get(i, 0)+1

    # 왼쪽 토핑부터 형한테 1개 추가, 동생한테 1개 반납
    for j in topping:
        if old.get(j, 0):
            old[j] += 1
        else:
            old[j] = 1

        if young.get(j, False):
            young[j] -= 1
            if young[j] == 0:
                young.pop(j)

        # 형 동생 토핑 수가 같아지면 +1
        if len(old) == len(young):
            answer += 1

        # 형 토핑 수가 많아지면 동생은 줄어드는 일만 있으니까 break
        elif len(old) > len(young):
            break

    return answer