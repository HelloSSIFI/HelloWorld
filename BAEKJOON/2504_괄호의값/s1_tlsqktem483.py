problem = input()

stack = []
ans = 0
temp = 1

for idx, br in enumerate(problem):
    if br == '(':
        stack.append(br)
        temp *= 2
    elif br == '[':
        stack.append(br)
        temp *= 3
    elif br == ')':
        if not stack or stack[-1] == '[':
            ans = 0
            break
        if problem[idx-1] == '(':
            ans += temp

        stack.pop()
        temp //= 2

    else:
        if not stack or stack[-1] == '(':
            ans = 0
            break
        if problem[idx - 1] == '[':
            ans += temp

        stack.pop()
        temp //= 3

if stack:
    print(0)
else:
    print(ans)