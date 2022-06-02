def check(idx, cnt):
    global result
    if cnt == K - 5:
        temp = 0
        for words in learning:
            for word in words:
                if not learned_check[ord(word) - ord('a')]:
                    break
            else:
                temp += 1
        result = max(result, temp)
        return

    for i in range(idx, 26):
        if not learned_check[i]:
            learned_check[i] = 1
            check(i, cnt+1)
            learned_check[i] = 0

N, K = map(int, input().split())
base = ['a', 'c', 'i', 'n', 't']
learned_check = [0] * 26
result = 0

for i in base:
    learned_check[ord(i) - ord('a')] = 1

learning = [set(input().lstrip('anta').rstrip('tica')) for _ in range(N)]

if K < 5:
    print(0)
    exit(0)
elif K == 26:
    print(N)
    exit(0)
else:
    check(0, 0)
    print(result)


#---------- 시간초과 ----------
#
# learning = set()
#
# def solution(spell):
#     cnt = 0
#     spell = set(spell)
#     for word in words:
#         com = set(word)
#         if com.difference(base) | spell == spell:
#             cnt += 1
#     return cnt
#
# if K < 5:
#     print(0)
# elif K == 26:
#     print(N)
# else:
#     for _ in range(N):
#         spelling = input().rstrip()
#         words.append(spelling)
#         spelling = spelling[4:-4]
#         temp = set(spelling).difference(base)
#         learning = learning | temp
#         for com in combinations(learning, K-5):
#             result = max(result, solution(list(com)))
#     print(result)
