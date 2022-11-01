S = input()
answer = len(S)
if len(set(S)) == 1: answer = -1        # 한 단어로만 이루어진 경우 무조건 팰린드롬
elif S == S[::-1]: answer -= 1          # 한 단어로 이루어진 문장이 아니고 전체 문장이 펠린드롬이면 끝에 한 글자만 빼면 펠린드롬이 아니게 됨
print(answer)
