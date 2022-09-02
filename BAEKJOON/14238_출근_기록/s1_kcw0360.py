work = list(input())
dp = dict()
ans = [0] * len(work)


def check(a, b, c, i):
    if i > 1 and dp.get((a, b, c, ans[i-1], ans[i-2])):    # 전날, 전전날 기록하여 중복 탐색 방지
        return

    if i == len(work):    # 순열이 완성된 경우 문자열로 만들어 출력
        print(''.join(ans))
        exit()

    if a > 0:    # 'A' 개수가 남아 있는 경우
        ans[i] = 'A'
        if i > 1:
            dp[(a, b, c, ans[i-1], ans[i-2])] = True
        check(a-1, b, c, i+1)

    if b > 0:    # 'B' 개수가 남아 있는 경우
        if i == 0 or ans[i-1] != 'B':    # 'B'가 첫날 출근 or 전날 출근하지 않았을 경우
            ans[i] = 'B'    # 'B' 출근
            if i > 1:    # i가 2 이상이 되어야 이틀전까지 기록이 가능
                dp[(a, b, c, ans[i-1], ans[i-2])] = True
            check(a, b-1, c, i+1)

    if c > 0:    # 'C' 개수가 남아 있는 경우
        # 'C'가 첫날 출근, 어제, 그저께 까지 출근하지 않아야 출근 가능
        if i == 0 or (i == 1 and ans[i-1] != 'C') or (i > 1 and ans[i-1] != 'C' and ans[i-2] != 'C'):
            ans[i] = 'C'
            if i > 1:
                dp[(a, b, c, ans[i-1], ans[i-2])] = True
            check(a, b, c-1, i+1)


check(work.count('A'), work.count('B'), work.count('C'), 0)
print(-1)    # 경우의 수가 없는 경우