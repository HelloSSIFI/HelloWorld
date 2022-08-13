import sys
input = sys.stdin.readline

original = input().strip()
pattern = list(input().strip())
stack = []

# replace와 in으로 하면 시간초과
# stack 사용

i = 0
while i < len(original):
    stack.append(original[i])                               # 문자열 push                                 
    if len(stack) - len(pattern) >= 0:                      # stack의 길이가 pattern의 길이와 같거나 크다면
        is_bomb = False
        for j in range(-1, -len(pattern)-1, -1):            # 마지막 문자열부터 비교하여 폭탄 문자열 탐색
            if stack[j] != pattern[j]:                      # stack에 하나씩 문자열을 넣을 때마다 탐색하므로 폭탄이 존재한다면 항상 stack의 마지막 패턴 길이만큼의 구간에 존재할 것
                is_bomb = False
                break
            is_bomb = True                                  
        
        if is_bomb:                                         # 폭탄 문자열이 현재 스택에 존재하면
            for _ in range(len(pattern)):                   # 폭탄 문자열 길이만큼 스택에서 pop
                stack.pop()
    i += 1

if stack:
    print(''.join(stack))
else:
    print('FRULA')

