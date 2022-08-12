def solution(n,a,b):
    answer = 0
    while a != b:               # a와 b가 붙을때까지
        a = (a + 1) // 2        # 다음 라운드 번호를 주고
        b = (b + 1) // 2        # answer+1
        answer += 1
    return answer
