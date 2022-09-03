def make(AB_cnt, word):
    global cnt                              # 조건에 맞는 문자열 개수가 1개씩 늘어나도록
    word_cnt = 0                            # 오른쪽부터 C를 word로 변경해 왼쪽으로 옮겨서
    i = -1                                  # 개수를 1씩 증가시킴
    while cnt < K:
        if i < 0 or answer[i] != 'C':       # 현재 자리가 인덱스를 벗어났거나 C가 아니면
            word_cnt += 1                   # 사용된 문자개수를 1 올려주고 인덱스를 개수에 맞게 옮겨줌
            i = N - 1 - word_cnt
            if word_cnt > AB_cnt:           # 사용된 문자개수를 넘어섰다면 반복종료
                break
        answer[i] = word                    # 현재 C 문자를 word로 바꿔주고
        answer[i + 1] = 'C'                 # 이전에 word였던 문자를 C로 바꿔줌
        i -= 1                              # 인덱스는 왼쪽으로 이동
        cnt += 1                            # 조건에 맞는 문자 개수 + 1


N, K = map(int, input().split())            # 문자열을 3등분해서 순서대로 A,B,C를 채우는게 조건을 만족하는 경우가 가장 큼

A = N // 3                                  # 만약 3등분이 되지 않는다면 나머지가 있는만큼 A,B 순서로 추가
if N % 3:                                   # A,B,C 개수를 구해줌
    A += 1

B = (N - A) // 2
if (N - A) % 2:
    B += 1

C = N - A - B

if A * (N - A) + B * C < K:                 # 3등분해서 최대로 나올 수 있는 조건 개수를 넘는다면 -1 출력
    print(-1)
    exit()

answer = ['C'] * N                          # 우선 문자열을 C로 채워줌
cnt = 0                                     # cnt가 K가 될 동안 A와 B를 각각 채워줌
make(A, 'A')                                # A개수만큼 A를 채워줌, 이 때 cnt가 1씩 늘어날 수 있도록 자리를 배치
make(B, 'B')                                # B도 마찬가지

print(''.join(answer))
