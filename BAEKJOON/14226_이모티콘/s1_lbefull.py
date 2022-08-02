from collections import defaultdict


S = int(input())
dp = [{1: {0}}, {0: {0}, 1: {1}}, {0: {0}, 1: {1}, 2: {1}}]

while S not in dp[-1]:                                      # dp의 각 요소는 key에 나올 수 있는 숫자가 들어가고
    temp = defaultdict(set)                                 # value에 해당 숫자의 클립보드에 복사될 수 있는 경우를 저장
    for k, v in dp[-1].items():                             # 이전 숫자들을 순회
        if k == 0:                                          # 숫자가 0이면 다음반복
            continue

        temp[k].add(k)                                      # 자신을 복사할 수 있으므로 자신을 경우의 수에 넣어줌
        if k - 1 >= 0:                                      # 이모티콘 하나 삭제는 클립보드를 건드리지 않으므로
            temp[k - 1].update(v)                           # k - 1의 숫자에 현제 클립보드 내용을 다 넣어줌
        for el in v:                                        # 클립보드의 숫자를 순회
            temp[k + el].add(el)                            # 클립보드 붙여넣기한 숫자에 클립보드 내용을 추가하면서 넣어줌
    dp.append(temp)

print(len(dp) - 1)
