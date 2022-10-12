def get(sub):
    sub = list(sub)
    length = len(sub)
    cnt = 0    
    stack = []
    for i in range(length):
        stack.append(sub[i])

        # '1', '1', '0' 거르고 나머지만 뽑아내기
        while stack[-3:] == ['1', '1', '0']:
            cnt += 1
            k = 0
            while k < 3:
                stack.pop()
                k += 1
    return stack, cnt


def insert(rest, cnt):
    result = []
    inserted = ['1', '1', '0']
    front_last = 0
    flag = True
    
    # 3개씩 비교해서 '110' 보다 작으면 i+1 슬라이딩
    for i in range(len(rest)):
        k = 0
        comp = rest[i:i+3]
        for c in comp:
            if c < inserted[k]:
                break
            k += 1
        else:
            front_last = i - 1
            flag = False
            break
    if flag:
        result = rest + inserted * cnt
    else:                    
        if front_last < 0:
            result = inserted * cnt + rest
        else:
            result = rest[:front_last + 1] + inserted * cnt + rest[front_last + 1:]
    return ''.join(result)

def solution(s):
    answer = []
    for sub in s:
        rest, cnt = get(sub)
        answer.append(insert(rest, cnt)) 
    return answer

solution(['1110', '100111100', "0111111010"])


### best solution
# def f(n):
#     stk = []
#     cnt = 0
#     for i in n:
#         stk.append(i)
#         if i == '0' and stk[-3:] == ['1', '1', '0']:
#             del stk[-3:]
#             cnt += 1
#     idx = -1
#     for i in range(len(stk)):
#         if stk[i] == '0':
#             idx = i
#     if idx < 0:
#         ret = "110"*cnt + ''.join(stk)
#     else:
#         ret = ''.join(stk[:idx+1]) + "110"*cnt + ''.join(stk[idx+1:])
#     return ret
# def solution(s):
#     return [f(x) for x in s]
