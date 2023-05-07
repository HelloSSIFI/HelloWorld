def solution(n, m, x, y, r, c, k):
    k -= (abs(x-r) + abs(y-c))    # k -= 목표지점까지 최소 이동거리

    # 이동할 수 있는 거리보다 목표지점이 먼 경우 현재 k는 음수
    # k가 홀수인 경우(목표지점에서 다른 곳으로 이동했다가 다시 돌아와야하기 때문에 반드시 k는 짝수가 남아야 한다.)
    if k < 0 or k % 2:
        return 'impossible'

    direction = {'d': 0, 'l': 0, 'r': 0, 'u': 0}

    # 목표지점까지 최소 이동거리로 갈 때 방향 개수를 체크한다.
    if x > r:
        direction['u'] += x - r
    else:
        direction['d'] += r - x
    if y > c:
        direction['l'] += y - c
    else:
        direction['r'] += c - y

    # 목표지점까지 이동할 수 있는 최소거리를 배제하고 남은 이동 횟수를 가지고 이동한다.
    # 이때 사전순으로 가장 빠른 d 방향으로 이동가능한지 체크
    # k의 남은 횟수 절반(편도)과 현 위치에서 d 방향으로 갈 수 있는 최대 거리 중 더 작은 값을 추가값으로 가진다.
    dp = min(k//2, n - (x + direction['d']))
    k -= 2 * dp    # 왕복이기 때문에 * 2 소모 (나머지는 u으로 사용)

    # 마찬가지로 l도 같은 방법으로 추가 이동 거리를 체크한다.
    lp = min(k//2, y - direction['l'] - 1)
    k -= 2 * lp

    # 사전순으로 인해 d, l 순으로 최대한 이동하면 (n,1)지점에 머무른다. 이때 이동할 수 있는 k가 더 남아있다면
    # 사전순으로 빠른 'rl'로 반복하여 소모한다.
    # 최종적으로 answer는 사전순을 따르며 각 개수대로 방향을 추가하여 문자열을 만들어준다.
    return 'd' * (direction['d']+dp) + 'l' * (direction['l']+lp)+ 'rl' * (k//2) +\
             'r' * (direction['r']+lp) +'u' * (direction['u']+dp)