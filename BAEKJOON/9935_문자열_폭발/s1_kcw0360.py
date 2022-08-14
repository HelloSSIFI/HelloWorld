S = input()
explosion = list(input())

stack = []

for i in S:
    stack.append(i)    # stack에 문자추가
    # 폭발 문자열 마지막 문자와 현재 문자가 같고, stack 안에 마지막 문자들이 폭발 문자열과 같다면 stack에서 삭제
    if i == explosion[-1] and stack[-len(explosion):] == explosion:
        del stack[-len(explosion):]

if stack:
    print(''.join(stack))
else:
    print('FRULA')