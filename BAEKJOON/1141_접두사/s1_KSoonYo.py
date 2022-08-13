import sys
input = sys.stdin.readline

n = int(input())
arr = []
sub = []
for _ in range(n):
    arr.append(input().strip())


arr.sort(key=lambda x : len(x))
while arr:
    word = arr.pop()
    if not sub:
        sub.append(word)
    else:
        is_sub = False
        for w in sub:
            length = len(word)
            if word[:length] == w[:length]:
                is_sub = True
                break
        if is_sub:
            continue
        sub.append(word)

print(len(sub))