def convert(num, base):
    integer = '0123456789ABCDEF'
    q, r = divmod(num, base)
    if q == 0:
        return integer[r]
    else:
        return convert(q, base) + integer[r]

def solution(n, t, m, p):
    '''
    n진법, t번 내 차례가 돌아옴, 게임 참여 인원 m, 내 순서 p
    '''

    # 내가 말해야할 숫자들
    memo = []

    # 현재 숫자
    num, numlist = 0, '0'

    # 회전 수, 차례, 현재 숫자 중 말할 위치
    cycle, i, j = 0, 1, 0

    # t번 사이클이 돌 때까지 반복
    while i <= m*t:

        # 내가 말할 차례
        if i - cycle*m == p:
            memo.append(numlist[j])

        # 말할 위치 변경
        j += 1

        # 현재 숫자를 다 말했다면 숫자 + 1
        if j == len(numlist):
            num += 1
            # 진법에 맞춰 numlist 다시 구성
            numlist = convert(num, n)
            j = 0

        # 사이클 추가
        if i%m == 0:
            cycle += 1

        i += 1

    return ''.join(memo)

print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))
