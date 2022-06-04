N, K = map(int, input().split())             # K개 알파벳 가르칠 수 있고, N개 단어가 존재
arr = [set(input()) for _ in range(N)]       # 단어 목록

if K < 5:
    print(0)
    exit()

elif K == 26:
    print(N)
    exit()

result = 0                              # 배울 수 있는 단어의 수
learn = [0]*26                          # 배운 알파벳 / a, n, t, i, c는 이미 알고 있는걸로 간주


for b in ['a', 'n', 'c', 't', 'i']:
    learn[ord(b) - ord('a')] = 1


def dfs(k, idx):
    global result

    if k == K-5:                  # 가르칠 수 있는 알파벳 개수를 채웠으면
        tmp = 0                   # 현재 알고있는 알파벳으로 알 수 있는 단어 수
        for txt in arr:           # 단어 목록을 순회
            for t in txt:
                if not learn[ord(t) - ord('a')]:break
            else:
                tmp += 1                      # break없이 통과했으면 아는 단어므로 tmp += 1

        result = max(result, tmp)
        return

    for i in range(idx, 26):                  # 배워야할 알파벳 추가
        if not learn[i]:
            learn[i] = 1
            dfs(k+1, i)
            learn[i] = 0

dfs(0, 0)
print(result)
