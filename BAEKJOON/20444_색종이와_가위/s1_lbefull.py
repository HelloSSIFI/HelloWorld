n, k = map(int, input().split())
l = 0
r = n // 2                              # n을 2등분 했을 때 서로를 곱하는 크기가 가장 큼
while l <= r:                           # 따라서 최대 범위를 n / 2 로 설정
    m = (l + r) // 2                    # m번 자르면 m + 1 만큼 종이가 나뉘므로
    cnt = (m + 1) * (n - m + 1)         # 종이의 개수를 구해줌
    if cnt == k:                        # k를 만들었다면 YES 출력 후 종료
        print('YES')
        exit()
    if cnt < k:                         # k보다 작으면 숫자를 키워주고
        l = m + 1
    else:                               # k보다 크다면 숫자를 줄여줌
        r = m - 1
print('NO')
