import sys
input = sys.stdin.readline

def teach(k, i):
    global cnt
    if len(new_set) == k:
        temp_cnt = 0
        for word in new_words:
            if new_set >= word:
                temp_cnt += 1
        cnt = max(cnt, temp_cnt)
        return

    for j in range(i, len(char_set)):
        new_set.add(char_set[j])
        teach(k, j + 1)
        new_set.remove(char_set[j])

N, K = map(int, input().split())
default_set = {'a', 'n', 't', 'i', 'c'}
new_words = []
char_set = set()

answer = 0
for _ in range(N):
    word = input().strip()
    temp = set(word) - default_set
    if temp:
        char_set.update(temp)
        new_words.append(temp)
    else:
        answer += 1
        
char_set = list(char_set)
new_set = set()
if K < 5:
    answer = 0
elif len(char_set) + len(default_set) <= K:
    answer = N
else:
    cnt = 0
    teach(K - 5, 0)
    answer += cnt
print(answer)
