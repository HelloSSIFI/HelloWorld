def solution(n, k, arr):
    # 다리길이, 견딜 수 있는 무게, 트럭무게배열
    def bridge():
        nonlocal state, n, w
        tmp = False

        for truck in state:
            truck[1] += 1
            if truck[1] == n:
                tmp = True
        else:
            if tmp:
                val, _ = state.pop(0)
                w -= val
        return


    answer = 0
    state, w = [], 0

    idx = 0
    while idx < len(arr):
        bridge()
        now = arr[idx]

        if len(state) < n and w+now <= k:
            w += now
            state.append([now, 0])
            idx += 1

        answer += 1

    while state:
        bridge()
        answer += 1

    return answer