S = input()
bomb = input()
stack = []
result = []

cnt = 0
for i in range(len(S)):
    result.append(S[i])                 # 현재 글자를 result에 추가
    if S[i] == bomb[cnt]:               # 폭탄이 되는 글자의 cnt번째 글짜와 같다면
        cnt += 1                        # cnt + 1
    
    elif S[i] == bomb[0]:               # 폭탄이 되는 글자의 맨 첫 글자와 같다면
        stack.append(cnt)               # 현재 cnt를 stack에 저장하고
        cnt = 1                         # cnt를 1로 변경
    
    else:                               # 아니라면
        cnt = 0                         # cnt를 0으로 만들고 stack을 비워줌
        stack = []
    
    if cnt == len(bomb):                # cnt가 bomb의 길이와 같아진다면
        for _ in range(cnt):            # cnt만큼 result에서 제거하고
            result.pop()
        if stack:                       # stack이 남아있다면
            cnt = stack.pop()           # cnt를 stack의 top으로 설정
        else:                           # stack이 비었다면
            cnt = 0                     # cnt를 0으로 설정

result = ''.join(result)
if not result:
    result = 'FRULA'
print(result)
