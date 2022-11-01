import sys
input = sys.stdin.readline


words = list(input().rstrip())
n = len(words)
answer = -1    # 불가능한 경우(문자열의 문자가 모두 동일한 것으로 이루어 졌을 때 출력)
if n % 2:    # 문자열 길이가 짝수인 경우
    if words[:n//2] != words[n//2+1:][::-1]:    # 회문 확인
        answer = n
    elif words[:(n-1)//2] != words[(n-1)//2:n-1][::-1]:    # 문자 하나 줄인 후 회문 확인
        answer = n-1    # 모두 같은 문자가 아닌 이상 회문인 문자열에서 길이를 1만큼 줄이면 회문이 아니게됨
else:    # 홀수인 경우
    if words[:n//2] != words[n//2:][::-1]:
        answer = n
    elif words[:(n-1)//2] != words[(n-1)//2+1:n-1][::-1]:
        answer = n-1

print(answer)