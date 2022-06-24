N = int(input())
if N < 10:
    print(N)
num = 10
cnt = 9


def assemble(top, n, word):
    global cnt

    if n == M:      # 해당 숫자의 길이가 다 되면 감소하는 수인지 검사
        for i in range(1, n):
            if int(word[i-1]) <= int(word[i]):break
        else:
            cnt += 1
            if cnt == N:
                print(word)
                exit()

        return

    for i in range(top):
        new = word + str(i)
        assemble(i, n+1, new)




while num <= 1000000:
    M = len(str(num))       # 숫자의 길이
    top = str(num)[0]       # 가장 큰 수

    assemble(int(top), 1, str(top))
    num += 10**(M-1)
else:
    print(-1)
