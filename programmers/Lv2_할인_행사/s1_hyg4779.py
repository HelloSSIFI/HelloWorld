from collections import deque

def solution(want, number, discount):

    # 모든 want를 얻을 수 있는지 check
    def check():
        for k, v in d.items():
            if v[0] > v[1]:
                return False
        return True

    # 출력 값
    answer = 0

    # 필요한 물건들
    # key: 물건명, valeu: [사야되는 개수, 현재 개수]
    d = {w: [n, 0] for w, n in zip(want, number)}

    # discount 탐색, 현재 장바구니
    idx, cart = 0, deque([])

    while idx < len(discount):
        # 10개 이상 담았다면 그 이후 부터 하나씩 제거
        if idx >= 10:
            item = cart.popleft()
            if item in want:
                d[item][1] -= 1

        now = discount[idx]
        cart.append(now)

        if now in want:
            d[now][1] += 1

        if check():
            answer += 1

        idx += 1

    return answer